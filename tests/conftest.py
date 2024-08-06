import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.graph.neo4j_database import Neo4jConnectionManager
from app.config import config

@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)

@pytest.fixture(scope="module")
async def neo4j_manager():
    # Get the Neo4j URI from environment variable or use a default
    neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    
    manager = Neo4jConnectionManager(
        uri=neo4j_uri,
        user=config.NEO4J.USER,
        password=config.NEO4J.PASSWORD
    )
    await manager.wait_for_neo4j()
    yield manager
    await manager.close()