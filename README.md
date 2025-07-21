# Aarogya Hetu – AI-Powered Medical Assistant

Aarogya Hetu is a web-based AI medical assistant that analyzes symptoms provided by users and returns potential causes, suggested cures, and necessary precautions. The system supports both text and voice input and leverages a combination of structured medical data and Retrieval-Augmented Generation (RAG) to provide intelligent responses.

## Features

- Symptom analysis from user input
- Voice-to-text conversion using speech recognition
- AI-powered medical response generation (cause, cure, precautions)
- Retrieval-Augmented Generation (RAG) using LangChain
- Integrated structured CSV-based medical knowledge
- Simple and interactive web interface built with Flask

## Tech Stack

**Backend:**
- Python
- Flask
- LangChain
- ChromaDB (for document retrieval)
- SentenceTransformers (`all-MiniLM-L6-v2`)
- SpeechRecognition (Google Speech API)

**Frontend:**
- HTML
- CSS
- JavaScript (for audio capture and form handling)

**Data Sources:**
- `symptom_knowledge.csv`: Structured dataset mapping symptoms to causes, cures, and precautions
- `medical_notes.txt`: Unstructured medical reference content used in RAG

## Project Structure

