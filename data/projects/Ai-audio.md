# 🎙️ EduVoice — AI Lecture Learning Assistant

EduVoice is an AI-powered lecture learning assistant that converts **lecture audio into structured study material**.

A user provides a lecture, and EduVoice processes the content to produce useful learning resources such as **summaries, notes, key points, definitions, examples, revision questions, quizzes, and brainstorming questions**.

The project combines **Speech-to-Text, NLP, embeddings, vector search, RAG, and LLMs** to transform unstructured lecture content into student-friendly study material.

---

## 🚀 What EduVoice Does

```text
Lecture Audio
     ↓
Speech-to-Text
     ↓
Transcript
     ↓
Text Cleaning & Processing
     ↓
Sentence Tokenization
     ↓
Chunking
     ↓
Embeddings
     ↓
Vector Search / RAG
     ↓
LLM
     ↓
Study Material
```

### Generated Output

* 📝 Summary
* 📚 Detailed notes
* 🔹 Main topics & key points
* 📖 Important definitions
* 💡 Examples
* 🧮 Formulas when present
* 🔄 Comparisons
* 🎯 Exam-important points
* ⚡ Quick revision
* ❓ Revision questions
* 🧠 Quiz questions
* 💭 Brainstorming & critical-thinking questions

---

# 🧠 How It Works

## 1. Audio Input

The user provides a lecture audio file.

EduVoice uses a **Speech-to-Text model** to convert the audio into text.

```text
lecture.mp3
     ↓
Speech-to-Text
     ↓
Raw transcript
```

---

## 2. Text Processing

The transcript is cleaned before further processing.

The system removes unnecessary speech, filler words, repetition, and other irrelevant conversational content while preserving important technical information.

The text is then divided into sentences.

```text
Raw transcript
      ↓
Cleaning
      ↓
Sentence tokenization
```

---

## 3. Chunking

Large text is divided into smaller meaningful sections called **chunks**.

This makes the content easier to process and retrieve.

```text
Sentences
    ↓
Chunk 1
Chunk 2
Chunk 3
...
```

---

## 4. Embeddings

Each chunk is converted into a numerical vector called an **embedding**.

Embeddings represent the semantic meaning of the text.

```text
Text chunk
    ↓
Embedding model
    ↓
Vector
```

Similar concepts produce vectors that are closer together in vector space.

---

## 5. FAISS Vector Search

The embeddings are stored in **FAISS**, which allows fast similarity search.

When a question is asked, the question is also converted into an embedding.

```text
User question
      ↓
Question embedding
      ↓
FAISS similarity search
      ↓
Most relevant chunks
```

---

## 6. RAG

EduVoice uses **Retrieval-Augmented Generation (RAG)**.

Instead of asking the LLM to generate an answer without context, the system first retrieves relevant information and provides it to the LLM.

```text
User Question
      ↓
Embedding
      ↓
FAISS
      ↓
Relevant lecture chunks
      ↓
LLM
      ↓
Answer
```

This helps the model generate answers based on the actual lecture content.

---

## 7. LLM Generation

The retrieved content is provided to the **Gemini API** along with instructions.

The LLM understands the lecture context and generates structured learning material.

The prompt instructs the model to preserve important technical information, remove unnecessary speech, avoid hallucinating information, and generate content supported by the lecture.

---

# 🏗️ Project Architecture

```text
                    🎙️ Lecture Audio
                           │
                           ▼
                  ┌─────────────────┐
                  │  Speech-to-Text │
                  └────────┬────────┘
                           │
                           ▼
                     📝 Transcript
                           │
                           ▼
                 Text Cleaning / NLP
                           │
                           ▼
                  Sentence Tokenizer
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
                    ┌──────┴──────┐
                    │             │
              User Question      │
                    │             │
                    ▼             │
               Embedding         │
                    │             │
                    └──────┬──────┘
                           ▼
                  Similarity Search
                           │
                           ▼
                  Relevant Context
                           │
                           ▼
                      Gemini LLM
                           │
                           ▼
                 📚 Study Material
```

---

# 🛠️ Technologies Used

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| Python                | Core development                    |
| Speech-to-Text model  | Lecture transcription               |
| NLP                   | Text processing                     |
| Sentence Tokenization | Splitting transcript into sentences |
| Embeddings            | Converting text into vectors        |
| FAISS                 | Vector similarity search            |
| RAG                   | Context-aware information retrieval |
| Gemini API            | Content generation                  |
| Streamlit             | User interface                      |

---

# 📁 Example Project Structure

```text
EduVoice/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│
├── data/
│
├── utils/
│   ├── transcription.py
│   ├── preprocessing.py
│   ├── chunking.py
│   ├── embeddings.py
│   └── retrieval.py
│
└── notebooks/
    └── experiments.ipynb
```

---

# 🔄 Complete Workflow

```text
1. Upload lecture
       ↓
2. Transcribe audio
       ↓
3. Clean transcript
       ↓
4. Sentence tokenize
       ↓
5. Create chunks
       ↓
6. Generate embeddings
       ↓
7. Store embeddings in FAISS
       ↓
8. Retrieve relevant information
       ↓
9. Send context to Gemini
       ↓
10. Generate structured study material
       ↓
11. Display results to the user
```

---

# 🎯 Design Principle

EduVoice follows one important rule:

> **Generate learning material from the lecture content without inventing unsupported information.**

The system prioritizes important educational and technical information over filler speech and unnecessary repetition.

---

# 🔮 Future Improvements

Possible future improvements include:

* Real-time lecture transcription
* Multi-language lecture support
* Voice-based question answering
* Interactive quiz mode
* Ask-your-lecture chatbot
* Better citation/source tracking
* Persistent lecture storage
* Personalized learning recommendations
* Cloud deployment

---

# 👨‍💻 Learning Outcomes

This project demonstrates practical experience with:

* Speech-to-Text
* NLP preprocessing
* Text chunking
* Semantic embeddings
* Vector databases/search
* Retrieval-Augmented Generation
* LLM APIs
* Prompt engineering
* AI application development
* Streamlit deployment

---

## ⭐ Project Summary

**EduVoice transforms lecture audio into an interactive learning resource by combining speech recognition, NLP, semantic search, RAG, and generative AI.**

Instead of manually reviewing an entire lecture, students can use EduVoice to quickly understand, revise, and interact with the important information contained within it.
