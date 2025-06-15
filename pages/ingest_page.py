import streamlit as st

# Set page config - must be the first Streamlit command
st.set_page_config(
    page_title="Document Ingestion & Summarization",
    page_icon="📚",
    layout="wide"
)

from markitdown import MarkItDown
from genai_services import summarize_text, chunk_text
from chroma_services import ingest_documents
import tempfile
import os

# Custom CSS for better styling
st.markdown("""
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: purple;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #ffffff;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #1f77b4;
    }
    
    /* Buttons */
    .stButton>button {
        background-color: #1f77b4;
        color:purple;
        border-radius: 5px;
        padding: 0.5rem 1rem;
        border: none;
        width: 100%;
        margin-top: 1rem;
    }
    
    .stButton>button:hover {
        background-color: #1668a1;
        border: none;
    }
    
    /* File uploader */
    .stFileUploader {
        background-color:gray;
        padding: 0rem;
        border-radius: 5px;
        border: 2px dashed #1f77b4;
            
    }
    
    /* Success message */
    .success-message {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        color: #155724;
        margin: 1rem 0;
        border: 1px solid #c3e6cb;
    }
    
    /* Error message */
    .stAlert {
        background-color: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
        border-radius: 0.5rem;
        padding: 1rem;
    }
    
    /* Text area */
    .stTextArea>div>div>textarea {
        background-color: white;
        border: 1px solid #ced4da;
        border-radius: 5px;
    }
    
    /* Spinner */
    .stSpinner>div {
        border-color: #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📚 Document Ingestion & Summarization")
st.markdown("---")

# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    This tool helps you:
    - Upload and process documents
    - Generate summaries
    - Store content for AI-powered chat
    """)
    
    st.markdown("---")
    st.markdown("### Supported Formats")
    st.markdown("- Text files (.txt)")
    st.markdown("- PDF documents (.pdf)")
    st.markdown("- Markdown files (.md)")
    st.markdown("- HTML files (.html)")
    st.markdown("- Word documents (.docx)")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        "📄 Upload your document",
        type=["txt", "pdf", "md", "html", "docx"],
        help="Upload any supported document format"
    )

if uploaded_file:
    try:
        # Save to temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        # Convert to text using markitdown
        converter = MarkItDown()
        doc_text = converter.convert(tmp_path).text_content

        with col1:
            st.subheader("📝 Document Preview")
            st.text_area("Extracted Text", doc_text, height=200)

        # Summarize
        with st.spinner("🤔 Generating summary..."):
            summary = summarize_text(doc_text)
            
        with col2:
            st.subheader("📋 Summary")
            st.markdown(summary)
            
            if st.button("💾 Save to Database", type="primary"):
                with st.spinner("📥 Ingesting document..."):
                    chunks = chunk_text(doc_text)
                    ingest_documents(chunks)
                    st.markdown('<div class="success-message">✅ Document successfully ingested!</div>', unsafe_allow_html=True)
                
                if st.button("🤖 Go to Chatbot"):
                    st.switch_page("pages/chatbot_page.py")

    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        st.info("Please try uploading a different file or contact support if the issue persists.")
