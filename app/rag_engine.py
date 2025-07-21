import os
import pandas as pd
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Load and embed documents
loader = TextLoader("app/medical_notes.txt")
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
chunks = splitter.split_documents(docs)

embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma.from_documents(chunks, embedding, persist_directory="./chroma_db")
retriever = db.as_retriever()
llm = OpenAI()  # Use your OpenAI key via environment variable

qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Load symptom CSV once
csv_df = pd.read_csv("app/symptom_knowledge.csv")

def check_symptom_csv(user_input: str) -> str:
    for _, row in csv_df.iterrows():
        if row['Symptom'].lower() in user_input.lower():
            return f"""
🧠 Predicted Diagnosis:
1. Cause: {row['Cause']}
2. Cure: {row['Cure']}
3. Precautions: {row['Precaution']}

⚠️ This is not medical advice. Please consult a doctor.
"""
    return None  # If no match

def get_medical_response(query: str) -> str:
    from app.voice_to_text import transcribe_audio_if_needed
    query = transcribe_audio_if_needed(query)

    csv_result = check_symptom_csv(query)
    if csv_result:
        return csv_result
    response = qa_chain.run(query)
    return response + "\n\n⚠️ This is not medical advice. Please consult a doctor."
