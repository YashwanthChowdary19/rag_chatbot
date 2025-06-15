# RAG-Chatbot

A sophisticated Retrieval-Augmented Generation (RAG) chatbot built with Streamlit, leveraging OpenAI's language models and ChromaDB for efficient document storage and retrieval.

## 🚀 Features

- **Document Processing**
  - Automatic text chunking with configurable overlap
  - Smart document summarization
  - Efficient document storage using ChromaDB

- **Intelligent Chat Interface**
  - Context-aware responses
  - Real-time document querying
  - Multi-page Streamlit interface

- **Technical Capabilities**
  - Vector similarity search
  - Token-based text processing
  - Persistent document storage
  - Environment-based configuration

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Sufficient disk space for document storage

## 🛠️ Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd RAG-Chatbot
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# For Windows (PowerShell/Command Prompt):
.venv\Scripts\activate

# For Linux/Mac:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file in the root directory with:
```
MODEL_API_KEY=your_openai_api_key
MODEL_BASE_URL=your_model_base_url
MODEL_NAME=your_model_name
CHROMA_COLLECTION_NAME=your_collection_name
```

## 🏗️ Project Structure

```
RAG-Chatbot/
├── main.py                 # Main application entry point
├── pages/                  # Streamlit pages
│   ├── ingest_page.py     # Document ingestion interface
│   └── chatbot_page.py    # Chatbot interface
├── chroma_services.py     # ChromaDB integration services
├── genai_services.py      # OpenAI API integration services
├── data.txt              # Sample data for testing
├── requirements.txt      # Project dependencies
└── .env                 # Environment variables
```

## 📦 Dependencies

- **streamlit**: Web application framework
- **openai**: OpenAI API client
- **tiktoken**: Tokenizer for OpenAI models
- **chromadb**: Vector database for document storage
- **markitdown[all]**: Markdown processing utilities

## 🚀 Usage

### Document Ingestion
1. Navigate to the "Ingest" page
2. Upload your documents
3. Wait for processing to complete
4. Verify the documents are stored in the database

### Using the Chatbot
1. Go to the "Chatbot" page
2. Start a conversation
3. Ask questions related to your ingested documents
4. Receive contextually relevant responses

## 🔧 Technical Details

### Document Processing
- Text is chunked using configurable size and overlap
- Chunks are embedded using sentence transformers
- Documents are stored in ChromaDB for efficient retrieval

### Query Processing
- User queries are matched against stored documents
- Relevant context is retrieved using vector similarity
- Responses are generated using the OpenAI API

## 🛡️ Best Practices

1. **Document Management**
   - Use clear, well-formatted documents
   - Break large documents into manageable chunks
   - Regular database maintenance

2. **API Usage**
   - Monitor API usage and costs
   - Implement rate limiting
   - Secure API key management

3. **Performance**
   - Regular database optimization
   - Monitor response times
   - Cache frequently used queries

## 🔍 Troubleshooting

### Common Issues

1. **API Connection**
   - Verify API key configuration
   - Check API endpoint accessibility
   - Validate environment variables

2. **Document Processing**
   - Check document format compatibility
   - Verify text encoding
   - Monitor chunking parameters

3. **Database Issues**
   - Ensure sufficient disk space
   - Verify database connection
   - Check collection configuration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request



## 🙏 Acknowledgments

- OpenAI for providing the language models
- Streamlit for the web framework
- ChromaDB for vector storage capabilities 