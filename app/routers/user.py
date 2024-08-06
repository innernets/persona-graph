from fastapi import APIRouter, Depends
from app.graph.neo4j_database import Neo4jConnectionManager

router = APIRouter()

@router.post("/users/{user_id}")
async def create_user(user_id: str, neo4j_manager: Neo4jConnectionManager = Depends(Neo4jConnectionManager)):
    query = "MERGE (u:User {id: $user_id})"
    async with neo4j_manager.driver.session() as session:
        await session.run(query, user_id=user_id)
    return {"status": "User created successfully"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: str, neo4j_manager: Neo4jConnectionManager = Depends(Neo4jConnectionManager)):
    query = "MATCH (u:User {id: $user_id}) DETACH DELETE u"
    async with neo4j_manager.driver.session() as session:
        await session.run(query, user_id=user_id)
    return {"status": "User deleted successfully"}