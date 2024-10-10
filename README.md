# Innernet User Memory

Innernet User Memory is an innovative digital identity system that evolves with a user's digital footprint. By creating and maintaining a dynamic knowledge graph for each user, Innernet provides contextually rich information to any programming interface, particularly LLM-based systems, enabling unprecedented levels of personalization and user-centric experiences.

## Vision

At Innernet, we believe in a future where digital interactions are seamlessly personalized, respecting user privacy while delivering unparalleled value. Our mission is to empower developers and businesses to create user experiences that are not just tailored, but truly understand and grow with each individual user.

## Features

- Dynamic user knowledge graph construction
- Contextual query processing using RAG (Retrieval-Augmented Generation)
- Scalable and efficient graph storage with Neo4j
- FastAPI backend for high-performance API interactions
- OpenAI integration for advanced natural language processing
- Docker-based deployment for easy setup and scaling

## Installation and Setup

1. Clone the repository:
   ```
   git clone https://github.com/innernets/persona-graph.git
   cd innernet-user-memory
   ```

2. Ensure you have Docker and Docker Compose installed on your system.

3. Create a `.env` file in the app directory with the following content:
   ```
   NEO4J_URI=neo4j://neo4j:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_secure_password
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Start the services:
   ```
   docker-compose up -d
   ```

5. The API will be available at `http://localhost:8000`. You can access the API documentation at `http://localhost:8000/docs`.

## API Usage

### Create a New User

```bash
curl -X POST "http://localhost:8000/api/v1/users" -H "Content-Type: application/json" -d '{"user_id": "alice123"}'
```

### Ingest User Data

```bash
curl -X POST "http://localhost:8000/api/v1/ingest/alice123" -H "Content-Type: application/json" -d '{"content": "Alice is a software engineer who loves hiking and photography."}'
```

### Perform a RAG Query

```bash
curl -X POST "http://localhost:8000/api/v1/rag/alice123/query" -H "Content-Type: application/json" -d '{"query": "What are Alice'\''s hobbies?"}'
```

### Examples

See the [examples.ipynb](examples.ipynb) file for a sample product recommendation use case. 

Also see the [Concept Note](EderLabs_Innernet_ConceptNote.pdf) for a more detailed overview of the product offering for consumer focused use cases toward a personalised internet. 

## Supercharging Personalization: Use Cases

1. **E-commerce Product Recommendations**
   Innernet can analyze a user's browsing history, purchase patterns, and stated preferences to provide hyper-personalized product recommendations that evolve with the user's tastes over time.

2. **Content Streaming Platforms**
   By understanding a user's viewing habits, genre preferences, and even mood patterns, Innernet can help streaming services offer content suggestions that are uncannily accurate and timely.

3. **Personal Finance Apps**
   Innernet can help finance apps provide tailored advice by understanding a user's spending habits, financial goals, and risk tolerance, adapting as the user's financial situation changes.

4. **Health and Fitness Applications**
   By tracking a user's exercise routines, dietary preferences, and health goals, Innernet can assist in providing personalized workout plans and nutrition advice that adapts as the user's fitness journey progresses.



## Architecture

Innernet User Memory uses FastAPI for the backend, Neo4j for graph storage, and OpenAI for natural language processing. The entire system is containerized using Docker for easy deployment.

## License

This project is licensed under the MIT License.
