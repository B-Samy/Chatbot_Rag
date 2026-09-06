
import os
import re

import faiss
import nltk
import numpy as np
import pdfplumber
import streamlit as st
from google import genai
from nltk import sent_tokenize

import nltk

nltk.download("punkt_tab", quiet=True)
nltk.download("punkt", quiet=True)


st.set_page_config(
    page_title="ASK LAT-US",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.caption('Made by Shaheer Rangrej ')

if "GEMINI_API_KEY" not in st.secrets:
    st.error("GEMINI_API_KEY is missing from .streamlit/secrets.toml")
    st.stop()

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if "index" not in st.session_state:
    st.session_state.index = None

if "documents_ready" not in st.session_state:
    st.session_state.documents_ready = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "resume_name" not in st.session_state:
    st.session_state.resume_name = None

if "readme_names" not in st.session_state:
    st.session_state.readme_names = []

if "total_characters" not in st.session_state:
    st.session_state.total_characters = 0


def extract_pdf_text(uploaded_file):
    pages = []

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()

            if text:
                pages.append(text)

    return "\n".join(pages)


def extract_readme_text(uploaded_files):
    documents = []

    for file in uploaded_files:
        text = file.read().decode(
            "utf-8",
            errors="ignore"
        )

        documents.append(
            f"PROJECT README: {file.name}\n\n{text}"
        )

    return "\n\n".join(documents)


def preprocess(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def create_chunks(text, chunk_size=5):
    try:
        sentences = sent_tokenize(text)
    except LookupError:
        nltk.download("punkt")
        sentences = sent_tokenize(text)

    chunks = []

    for i in range(0, len(sentences), chunk_size):
        chunk = sentences[i:i + chunk_size]
        chunk_text = " ".join(chunk).strip()

        if chunk_text:
            chunks.append(chunk_text)

    return chunks


def create_index(chunks):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=chunks
    )

    embeddings = np.array(
        [
            embedding.values
            for embedding in response.embeddings
        ],
        dtype="float32"
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index


def ask_question(question):
    index = st.session_state.index
    chunks = st.session_state.chunks

    query_response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=question
    )

    query_embedding = np.array(
        [query_response.embeddings[0].values],
        dtype="float32"
    )

    k = min(5, len(chunks))

    distances, indices = index.search(
        query_embedding,
        k=k
    )

    relevant_chunks = [
        chunks[i]
        for i in indices[0]
        if i >= 0
    ]

    context = "\n\n".join(relevant_chunks)

    prompt = f"""
You are an AI assistant that answers questions about a user's resume and projects.

Use ONLY the context provided below.

Rules:

1. Do not invent information.
2. Do not use outside knowledge.
3. If the answer cannot be found in the context, say:
"I couldn't find the answer in the provided documents."
4. Give a clear and concise answer.
5. If multiple projects or skills are relevant, list them.
6. Preserve technical terminology.
7. Do not mention the RAG system.
8. Do not mention FAISS or embeddings unless the user specifically asks about them.

CONTEXT:

{context}

QUESTION:

{question}
"""

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    return response.text


st.markdown(
    """
    # ASK LAT-US
    ### Your personal resume and project knowledge assistant
    """
)

st.write(
    "Upload your resume and project documentation, then ask questions using natural language."
)

st.divider()


with st.sidebar:
    st.title("📂 Knowledge Base")

    st.caption(
        "Build your personal AI knowledge base from your resume and project documentation."
    )

    st.divider()

    st.subheader("Resume")

    resume_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        help="Upload your latest resume.",
        
    )

    if resume_file:
        st.success("Resume ready")
        st.caption(resume_file.name)

    st.divider()

    st.subheader("Projects")

    readme_files = st.file_uploader(
        "Upload README files",
        type=["md", "markdown", "txt"],
        accept_multiple_files=True,
        help="Upload project documentation."
    )

    if readme_files:
        st.success(
            f"{len(readme_files)} project file(s) ready"
        )

        for file in readme_files:
            st.caption(f"📘 {file.name}")

    st.divider()

    analyze_button = st.button(
        "🚀 Analyze Docs",
        use_container_width=True,
        type="primary"
    )

    if st.session_state.documents_ready:
        st.divider()

        st.subheader("System Status")

        st.success("Knowledge base ready")

        st.metric(
            "Documents",
            1 + len(st.session_state.readme_names)
        )

        st.metric(
            "Knowledge chunks",
            len(st.session_state.chunks)
        )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()


if analyze_button:
    if not resume_file:
        st.error(
            "Please upload your resume before building the knowledge base."
        )
    else:
        try:
            with st.status(
                "Building your knowledge base...",
                expanded=True
            ) as status:
                st.write("Reading resume")

                resume_text = extract_pdf_text(
                    resume_file
                )

                if not resume_text.strip():
                    st.error(
                        "Could not extract text from the resume."
                    )
                    st.stop()

                st.write("Reading project documentation")

                readme_text = ""

                if readme_files:
                    readme_text = extract_readme_text(
                        readme_files
                    )

                merged_text = f"""
RESUME:

{resume_text}

PROJECT README FILES:

{readme_text}
"""

                st.write("Cleaning document text")

                clean_text = preprocess(
                    merged_text
                )

                st.write("Creating knowledge chunks")

                chunks = create_chunks(
                    clean_text,
                    chunk_size=5
                )

                if not chunks:
                    st.error(
                        "No knowledge chunks were created."
                    )
                    st.stop()

                st.write("Generating semantic embeddings")

                index = create_index(
                    chunks
                )

                st.session_state.chunks = chunks
                st.session_state.index = index
                st.session_state.documents_ready = True
                st.session_state.resume_name = resume_file.name
                st.session_state.readme_names = [
                    file.name
                    for file in readme_files
                ] if readme_files else []
                st.session_state.total_characters = len(
                    clean_text
                )
                st.session_state.messages = []

                status.update(
                    label="Knowledge base ready",
                    state="complete",
                    expanded=False
                )

            st.success(
                f"Successfully processed {len(chunks)} knowledge chunks."
            )

        except Exception as e:
            st.error(
                f"Unable to process the documents: {e}"
            )


if st.session_state.documents_ready:
    st.subheader("Knowledge Base")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Resume",
            "Ready"
        )

    with col2:
        st.metric(
            "Projects",
            len(st.session_state.readme_names)
        )

    with col3:
        st.metric(
            "Knowledge chunks",
            len(st.session_state.chunks)
        )

    with col4:
        characters = st.session_state.total_characters

        if characters >= 1000:
            value = f"{characters / 1000:.1f}K"
        else:
            value = str(characters)

        st.metric(
            "Characters",
            value
        )

    with st.expander("View indexed documents"):
        st.write(
            f"📄 {st.session_state.resume_name}"
        )

        for name in st.session_state.readme_names:
            st.write(
                f"📘 {name}"
            )

    st.divider()


if not st.session_state.documents_ready:
    col1, col2, col3 = st.columns(3)

    with col1:
        st.info(
            """
            ### 📄 Upload

            Add your resume and project documentation from the sidebar.
            """
        )

    with col2:
        st.info(
            """
            ### 🧠 Analyze

            Build a searchable knowledge base from your documents.
            """
        )

    with col3:
        st.info(
            """
            ### 💬 Ask

            Ask natural-language questions about your experience and projects.
            """
        )

    st.divider()

    st.subheader("Example questions")

    example_col1, example_col2 = st.columns(2)

    with example_col1:
        st.write("• What are my strongest technical skills?")
        st.write("• Which projects use Python?")
        st.write("• Summarize my professional experience.")

    with example_col2:
        st.write("• What projects involve machine learning?")
        st.write("• What technologies did I use in my projects?")
        st.write("• Which project best demonstrates my backend skills?")


if st.session_state.documents_ready: 
    st.subheader("👋 Ask LAT-US AI")

    if not st.session_state.messages:
        st.caption(
            "Ask anything about your resume, skills, experience, or projects."
        )

    for message in st.session_state.messages:
        with st.chat_message(
            message["role"]
        ):
            st.markdown(
                message["content"]
            )

    question = st.chat_input(
        "Ask about your resume or projects..."
    )

    if question:
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Searching your knowledge base..."):
                try:
                    answer = ask_question(
                        question
                    )

                    st.markdown(answer)

                except Exception as e:
                    answer = (
                        f"Sorry, something went wrong: {e}"
                    )

                    st.error(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )


st.divider()

st.caption(
    "LAT-US AI • Gemini • FAISS • Streamlit"
)

