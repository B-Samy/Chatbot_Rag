# 🤖 Personal Knowledge RAG Chatbot

https://ai-chatbotrag.streamlit.app/

A document-based AI chatbot that allows users to upload **PDF and Markdown (`.md`) files** and ask questions about their content.

The system uses **NLP text processing, embeddings, FAISS vector search, Retrieval-Augmented Generation (RAG), and the Gemini LLM API** to retrieve relevant information from uploaded documents and generate accurate, context-based answers.

---

## 🚀 What the Project Does

```text
PDF / Markdown Files
        ↓
Text Extraction
        ↓
Basic Text Cleaning
        ↓
Sentence Tokenization
        ↓
Chunking
        ↓
Text Embeddings
        ↓
FAISS Vector Database
        ↓
User Question
        ↓
Question Embedding
        ↓
Similarity Search
        ↓
Relevant Chunks
        ↓
Gemini LLM
        ↓
🤖 Final Answer
```

---

# 🎯 Objective

The goal is to build a chatbot that can **understand and answer questions from the user's own documents**.

For example, a user can upload:

```text
📁 Documents
├── resume.pdf
├── README.md
├── project.md
└── architecture.md
```

Then ask:

> **Which project converts lectures into notes?**

The system searches the uploaded documents, retrieves the relevant information, and sends it to Gemini to generate the answer.

---

# 📄 Supported Documents

The chatbot can work with:

- PDF files
- Markdown (`.md`) files

Markdown files can contain:

- README files
- Project documentation
- Technical notes
- Architecture documents
- Project descriptions
- Personal documentation

---

# 🧹 1. Text Extraction & Cleaning

The uploaded documents are first converted into text.

```text
PDF
 ↓
Extract text

MD
 ↓
Read file
```

The extracted content is then cleaned by removing unnecessary formatting, excessive whitespace, and other unwanted text while preserving meaningful information.

---

# ✂️ 2. Sentence Tokenization

The cleaned text is divided into individual sentences.

```text
Document
   ↓
Sentence 1
Sentence 2
Sentence 3
Sentence 4
...
```

Sentence-level processing helps create more meaningful chunks for retrieval.

---

# 🧩 3. Chunking

Large documents are divided into smaller groups of sentences called **chunks**.

Example:

```text
Chunk 1
→ Sentence 1
→ Sentence 2
→ Sentence 3
→ Sentence 4
→ Sentence 5

Chunk 2
→ Sentence 6
→ Sentence 7
→ Sentence 8
→ Sentence 9
→ Sentence 10
```

Chunking allows the system to search smaller and more relevant sections instead of processing the entire document for every question.

---

# 🧠 4. Embeddings

Each chunk is converted into a numerical vector using an embedding model.

```text
Text Chunk
    ↓
Embedding Model
    ↓
Vector
```

The vector represents the semantic meaning of the chunk.

The user's question is also converted into an embedding so that it can be compared with the document vectors.

---

# 🔎 5. FAISS Vector Search

The document embeddings are stored in **FAISS**.

When the user asks a question:

```text
User Question
      ↓
Question Embedding
      ↓
FAISS Similarity Search
      ↓
Most Relevant Chunks
```

FAISS retrieves the chunks that are semantically closest to the user's question.

---

# 🔗 6. Retrieval-Augmented Generation (RAG)

The project uses **RAG** to connect document retrieval with the LLM.

Instead of sending every document directly to the LLM, the system first retrieves the most relevant chunks.

```text
User Question
      ↓
FAISS
      ↓
Relevant Context
      ↓
Gemini
      ↓
Answer
```

This allows the chatbot to answer questions using information from the user's uploaded documents.

---

# 🤖 7. Gemini LLM

The retrieved chunks are provided to the **Gemini API** together with the user's question.

The LLM uses this context to generate the final response.

The chatbot is instructed to:

- Use the retrieved context
- Avoid inventing information
- Answer clearly
- State when the information cannot be found in the provided documents

---

# 🏗️ Project Architecture

```text
                     📄 PDF / MD
                          │
                          ▼
                 Text Extraction
                          │
                          ▼
                   Text Cleaning
                          │
                          ▼
               Sentence Tokenization
                          │
                          ▼
                      Chunking
                          │
                          ▼
                     Embeddings
                          │
                          ▼
                       FAISS
                          │
                          │
                 ┌────────▼────────┐
                 │                 │
           User Question           │
                 │                 │
                 ▼                 │
          Question Embedding       │
                 │                 │
                 └────────┬────────┘
                          ▼
                  Similarity Search
                          │
                          ▼
                   Relevant Chunks
                          │
                          ▼
                     Gemini LLM
                          │
                          ▼
                    🤖 Answer
                          │
                          ▼
                    Streamlit UI
```

---

# 🔄 Complete Workflow

```text
1. Upload PDF / MD files
        ↓
2. Extract or read text
        ↓
3. Perform basic cleaning
        ↓
4. Sentence tokenize
        ↓
5. Create text chunks
        ↓
6. Generate embeddings
        ↓
7. Store vectors in FAISS
        ↓
8. User asks a question
        ↓
9. Generate question embedding
        ↓
10. Search FAISS
        ↓
11. Retrieve relevant chunks
        ↓
12. Send context + question to Gemini
        ↓
13. Generate final answer
        ↓
14. Display answer in Streamlit
```

---

# 🛠️ Technologies Used

| Technology            | Purpose                                |
| --------------------- | -------------------------------------- |
| Python                | Core development                       |
| NLP                   | Text processing                        |
| Sentence Tokenization | Splitting documents into sentences     |
| Embedding Model       | Creating semantic vectors              |
| FAISS                 | Vector similarity search               |
| RAG                   | Context-based retrieval and generation |
| Gemini API            | Answer generation                      |
| Streamlit             | Chatbot interface                      |

---

# 📁 Suggested Project Structure

```text
RAG-Chatbot/
│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── documents/
│
├── models/
│
├── src/
│   ├── document_loader.py
│   ├── preprocessing.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   └── llm.py
│
└── notebooks/
    └── rag_experiments.ipynb
```

---

# 💬 Example

### User uploads

```text
resume.pdf
README.md
EduVoice.md
fraud_detection.md
```

### User asks

> Which project converts lectures into notes?

### RAG process

```text
Question
   ↓
Embedding
   ↓
FAISS
   ↓
Relevant EduVoice chunk
   ↓
Gemini
```

### Chatbot

```text
🤖 EduVoice is the project that converts
lecture audio into text and generates
structured learning material such as notes,
summaries, and key points.
```

---

# 🌐 Streamlit Application

The final application provides a simple chat interface where users can:

- Upload PDF files
- Upload Markdown files
- Process documents
- Ask questions
- Receive AI-generated answers
- Continue the conversation

Example:

```text
┌──────────────────────────────────────┐
│ 🤖 Personal Knowledge Chatbot        │
├──────────────────────────────────────┤
│                                      │
│ 📎 Upload PDF / MD                   │
│                                      │
│ You: Which project uses RAG?         │
│                                      │
│ 🤖: Based on your documents, ...     │
│                                      │
│ 📚 Retrieved source: README.md       │
│                                      │
│ [ Ask a question...              ]   │
└──────────────────────────────────────┘
```

---

# 🔐 RAG Answering Rule

The chatbot should follow a simple principle:

> **Answer using the retrieved document context. If the required information cannot be found, clearly tell the user instead of inventing an answer.**

This helps reduce hallucinations and makes the chatbot more reliable.

---

# 🔮 Future Improvements

Possible improvements include:

- Conversation memory
- Multiple-document source tracking
- Source citations
- Streaming responses
- Chat history
- Document management
- Hybrid search
- Better chunking strategies
- Reranking retrieved chunks
- Support for DOCX and TXT
- Image/document understanding
- Voice input and output
- User authentication

---

# 🎓 Learning Outcomes

This project demonstrates practical experience with:

- NLP
- Text preprocessing
- Sentence tokenization
- Text chunking
- Semantic embeddings
- Vector databases
- FAISS similarity search
- Retrieval-Augmented Generation
- LLM APIs
- Prompt engineering
- Document question answering
- Streamlit application development

---

## ⭐ Project Summary

**Personal Knowledge RAG Chatbot** is an AI-powered document question-answering system that allows users to chat with their own PDF and Markdown files.

The project combines:

**Document Processing → NLP → Chunking → Embeddings → FAISS → RAG → Gemini → Streamlit**

to create a chatbot capable of retrieving relevant information from personal documents and generating context-aware answers.
