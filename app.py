import streamlit as st
from resume_handler import extract_text_from_pdf
from rag_pipeline import build_rag_bot
import openai
import os

# Setup your OpenAI key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Resume Q&A Bot", page_icon="🧠")
st.title("🧠 Chat with Your Resume")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type="pdf")

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    st.success("✅ Resume uploaded and parsed successfully!")

    # Build RAG pipeline
    qa_chain = build_rag_bot(resume_text)

    query = st.text_input("💬 Ask something about your resume")

    if query:
        with st.spinner("Thinking..."):
            response = qa_chain.run(query)
        st.markdown("**Answer:**")
        st.write(response)
