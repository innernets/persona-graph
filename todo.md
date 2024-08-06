Milestone 1 TODO:
1. Setup Project Structure
-->
2. Define MVP 
3. Define Inputs / Outputs
4. Define sub tasks 
5. Write tests


Graph:

- Develop graph functions assuming neo4j for now. 
- Make functions to add, remove user, node, relationship
- Setup properties for nodes
- input preferences for the graph schema`
- Write a RAG system -> Ask Question -> Get response

### Module Design and Development Steps

- **FastAPI Setup:**
  - [x] Check for neo4j server setup
  - [x] Serve the API
  - [ ] Serve CRUD APIs

- **Neo4j Integration:**
  - [x] Docker Setup: Include Neo4j in `docker-compose.yml`.
  - [x] Database Connection Module: Create a module that initializes and configures the Neo4j connection using its Python driver.
  - [x] User Registration: Hardcode user for dev in the app
  - [x] Simulate a user registration function that can take a user ID or details and creates a corresponding node in the Neo4j database.

- **Core Graph Functionality Module:**
  - [x] CRUD : Implement functions to add and manage nodes, edges, and properties in the graph. This should handle basic CRUD operations on the graph elements.
  - [x] Implement vector index and embedding generation
  - [x] Implement vector search

- **Data Preprocessing Module:**
  - [x] Create a utility that converts unstructured data into a structured format that the graph constructor can use.
  - [x] Entity Generation

- **Graph Constructor with LLM:**
  - [ ] Design a graph schema file
  - [x] Design a module that takes either an entity list or user context and processes it through a language model to generate or update graph structures.
  - [x] Ensure this module can interact with the LLM effectively and integrate the results back into the graph using core module
  - [x] Fetch the complete context to update the graph

- **Graph Reading Module:**
  - [x] Develop functions to query the graph and extract relevant data based on the user context or specific queries.

- **Query and Response Module:**
  - [ ] Ask anything. Implement functionalities to write complex queries to the graph and format the LLM responses to structured data

- **API:**
  - [ ] Add API endpoints for the above functions
  - [ ] Serve APIs server
  - [ ] Write documentation

# First Release:

1. Package the Application:
   - [ ] Create a setup.py file for packaging
   - [ ] Define package dependencies
   - [ ] Write a README.md with installation and usage instructions

2. Documentation:
   - [ ] Create API documentation for all endpoints
   - [ ] Write a quickstart guide
   - [ ] Provide example usage for each main feature

3. GitHub Repository Setup:
   - [ ] Initialize git repository
   - [ ] Create .gitignore file
   - [ ] Add LICENSE file (choose an appropriate open-source license)

4. PyPI Publication:
   - [ ] Create an account on PyPI
   - [ ] Prepare the package for PyPI
   - [ ] Publish the package to PyPI

5. Example Integration:
   - [ ] Create a simple example project demonstrating how to use the library

6. Testing:
   - [ ] Write unit tests for core functionality
   - [ ] Create integration tests for API endpoints

7. Error Handling:
   - [ ] Implement comprehensive error handling
   - [ ] Create meaningful error messages for API responses

8. Versioning:
   - [ ] Implement semantic versioning
   - [ ] Create a CHANGELOG.md file

9. Documentation Website:
   - [ ] Set up a simple documentation website (e.g., using GitHub Pages)

10. Cleanup:
    - [ ] Remove any hardcoded values or development shortcuts
    - [ ] Ensure all TODOs in the code are addressed

---------

# RAG Interface Improvements TODO:

1. Query Understanding:
   - [ ] Implement query rewriting and expansion method
   - [ ] Add support for metadata (e.g., date ranges, domain filters) in queries

2. Context Retrieval:
   - [ ] Implement multi-backend search (combine vector and graph-based search)
   - [ ] Add query planning for complex questions

3. Use Case Context
   - [ ] Implement a script to generate a graph schema 
   - [ ] add Dynamic context for graph construction prompt

   
4. Testing and Evaluation:
   - [ ] Create test cases for each new feature
   - [ ] Implement evaluation metrics for response quality
   - [ ] Test with Youtube Data and Email Data

5. Documentation:
   - [ ] Update API documentation for new methods
   - [ ] Create usage examples for new features

6. Optimization:
   - [ ] Profile and optimize performance of new features
   - [ ] Implement caching for frequently accessed data



-----------

### Tasks

- [x] Send a batch of nodes and embeddings to the graph_ops, and batch process. 
- [ ] OpenAI , JSON output format error for nodes and relationships generation. Add validation check
- [ ] Control the model being used in a config file. 
- [ ] Connect Central Nodes with the User Node. 
- [ ] Add richer graph context 
- [ ] Quantify frequency and recency of nodes:
- [ ] Unstructured Data ingestion guidelines and parameters. 