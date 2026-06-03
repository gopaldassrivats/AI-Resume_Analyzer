import streamlit as st
from resume_parser import extract_text
from rag import create_vectorstore
from llm import analyze

st.title("AI Resume Analyzer")

resume = st.file_uploader(
    "Upload Resume",
    type="pdf"
)

jd = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze"):

    if resume and jd:

        resume_text = extract_text(resume)

        st.write("Resume extracted successfully")
        st.write("Job Description:", jd)

        db = create_vectorstore(jd)

        docs = db.similarity_search(
            resume_text,
            k=3
        )

        context = ""

        for doc in docs:
            context += doc.page_content

        result = analyze(
            resume_text,
            context
        )

        st.write("Result:")
        st.write(result)