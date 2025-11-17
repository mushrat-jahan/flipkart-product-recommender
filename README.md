# Flipkart Product Recommender

A RAG (Retrieval-Augmented Generation) based chatbot for product recommendations using Flipkart product reviews. The system uses LangChain, AstraDB for vector storage, and Groq LLM to provide intelligent product recommendations based on user queries.

## Features

- Product recommendation based on reviews and product titles
- Conversational interface with chat history
- RAG architecture for accurate, context-aware responses
- Vector search using AstraDB
- Real-time product insights from customer reviews
- Prometheus metrics integration
- Dockerized deployment

## Technology Stack

- **Backend**: Flask
- **LLM**: Groq (llama-3.1-8b-instant)
- **Embeddings**: HuggingFace (BAAI/bge-base-en-v1.5)
- **Vector Database**: AstraDB
- **Orchestration**: LangChain
- **Monitoring**: Prometheus
- **Deployment**: Docker, Kubernetes

## Project Structure

```
flipkart-product-recommender/
├── flipkart/
│   ├── __init__.py
│   ├── config.py              # Configuration management
│   ├── data_converter.py      # CSV to Document converter
│   ├── data_ingestion.py      # Data ingestion to vector store
│   └── rag_chain.py           # RAG chain implementation
├── utils/
│   ├── __init__.py
│   ├── custom_exception.py    # Custom exception classes
│   └── logger.py              # Logging configuration
├── templates/
│   └── index.html             # Chat interface
├── static/
│   └── style.css              # Styling
├── Data/
│   └── flipkart_product_review.csv
├── app.py                     # Flask application
├── Dockerfile
├── flask-deployment.yaml      # Kubernetes deployment
├── requirements.txt
└── setup.py

```

## Prerequisites

- Python 3.8+
- AstraDB account (for vector database)
- Groq API key

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd flipkart-product-recommender
```

### 2. Create virtual environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -e .
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
ASTRA_DB_API_ENDPOINT=your_astradb_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_astradb_token
ASTRA_DB_KEYSPACE=your_keyspace
GROQ_API_KEY=your_groq_api_key
```

### 5. Ingest data (first time only)

```bash
python flipkart/data_ingestion.py
```

This will:
- Load product reviews from CSV
- Convert them to document format
- Create embeddings
- Store in AstraDB vector database

### 6. Run the application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Docker Deployment

### Build Docker image

```bash
docker build -t flipkart-recommender .
```

### Run container

```bash
docker run -p 5000:5000 \
  -e ASTRA_DB_API_ENDPOINT=your_endpoint \
  -e ASTRA_DB_APPLICATION_TOKEN=your_token \
  -e ASTRA_DB_KEYSPACE=your_keyspace \
  -e GROQ_API_KEY=your_key \
  flipkart-recommender
```

## Kubernetes Deployment

```bash
kubectl apply -f flask-deployment.yaml
```

## API Endpoints

- `GET /` - Chat interface
- `POST /get` - Get chatbot response
  - Form parameter: `msg` (user message)
  - Returns: Bot response (text)
- `GET /metrics` - Prometheus metrics

## Usage Example

1. Open the web interface at `http://localhost:5000`
2. Type your product query, e.g.:
   - "What are good bluetooth headphones?"
   - "Show me budget smartphones with good battery"
   - "Which laptop is best for gaming?"
3. The chatbot will analyze reviews and provide recommendations

## Architecture

1. **Data Ingestion**: CSV data is converted to LangChain documents with product title metadata
2. **Vector Store**: Documents are embedded and stored in AstraDB
3. **RAG Chain**:
   - User query is contextualized with chat history
   - Relevant reviews are retrieved from vector store
   - LLM generates response based on retrieved context
4. **Chat History**: Maintains conversation context per session

## Configuration

Key configurations in [flipkart/config.py](flipkart/config.py):

- `EMBEDDING_MODEL`: HuggingFace embedding model
- `RAG_MODEL`: Groq LLM model
- Database credentials from environment variables

## Monitoring

Prometheus metrics are exposed at `/metrics` endpoint for monitoring:

- HTTP request counts
- Response times
- Error rates

## Development

### Running in debug mode

```bash
python app.py
```

Debug mode is enabled by default in `app.py`.

### Adding new features

1. Modify the RAG chain in [flipkart/rag_chain.py](flipkart/rag_chain.py)
2. Update prompts for different behavior
3. Adjust retrieval parameters (currently k=3)

## Troubleshooting

### Import errors
Make sure you've installed the package: `pip install -e .`

### Database connection issues
Verify your AstraDB credentials in `.env`

### No responses from chatbot
Check if data ingestion completed successfully and vector store is populated

## License

MIT

## Author

Mushrat

## Contributing

Pull requests are welcome. For major changes, please open an issue first.
