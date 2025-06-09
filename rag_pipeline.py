from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def build_rag_bot(resume_text):
    # Split text
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(resume_text)

    # Create embedding
    embedding = OpenAIEmbeddings()
    
    # Vectorstore
    vectordb = Chroma.from_texts(chunks, embedding)
    
    # Retrieval-based QA
    qa_chain = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=vectordb.as_retriever())
    
    return qa_chain
