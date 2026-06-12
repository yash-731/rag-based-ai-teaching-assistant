# RAG Based AI Teaching Assistant

A Retrieval-Augmented Generation (RAG) based AI assistant that answers course-related questions using video transcripts.

## Features

- Converts course videos into transcripts
- Splits transcripts into semantic chunks
- Generates embeddings using BGE-M3
- Retrieves relevant chunks using cosine similarity
- Uses Llama 3.2 through Ollama for answer generation
- Provides timestamp-aware responses so users can directly jump to relevant sections of a course

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Ollama
- BGE-M3 Embeddings
- Llama 3.2

## How It Works

1. Video is converted into transcript.
2. Transcript is divided into chunks.
3. Embeddings are generated and stored.
4. User asks a question.
5. Relevant chunks are retrieved using semantic similarity search.
6. Retrieved context is passed to Llama 3.2 to generate an answer.

## Example Query

**Question:**
```
What are input tags in HTML?
```

**Response:**
```
Input tags are covered in the HTML Forms section. Check Video 7 around the relevant timestamp for a detailed explanation.
```

## Current Status

This project currently indexes and retrieves information from **a single course video transcript**.

The current implementation demonstrates:
- Transcript processing
- Embedding generation
- Semantic retrieval
- RAG-based answering

### Planned Improvements

- Support for multiple videos
- Vector database integration (FAISS/ChromaDB)
- Better retrieval ranking
- Web interface
- Course-wide search across all lessons

## Learning Outcome

This project helped me understand:
- Retrieval-Augmented Generation (RAG)
- Embeddings and semantic search
- Prompt engineering
- Local LLM deployment with Ollama
- End-to-end AI application development

## Author

Yash Saxena
