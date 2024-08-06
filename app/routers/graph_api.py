from fastapi import APIRouter, HTTPException, status
from app.graph.graph_ops import GraphOps
from app.utils.models import NodeModel, RelationshipModel, GraphUpdateModel
from app.graph.constructor import GraphConstructor
from app.openai.prompts import sample_statements, ASTRONAUT_PROMPT, SPACE_SCHOOL_CHAT
from app.utils.models import UnstructuredData
from app.graph.constructor import GraphContextRetriever
from app.graph.rag_interface import RAGInterface
from app.utils.models import UserCreate, IngestData, RAGQuery, RAGResponse
from app.api.user_service import UserService
from app.api.ingest_service import IngestService
from app.api.rag_service import RAGService
import random

router = APIRouter()


@router.post("/users", status_code=201)
async def create_user(user: UserCreate):
    try:
        await UserService.create_user(user.user_id)
        return {"message": f"User {user.user_id} created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    try:
        await UserService.delete_user(user_id)
        return {"message": f"User {user_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/ingest/{user_id}")
async def ingest_data(user_id: str, data: IngestData):
    try:
        await IngestService.ingest_data(user_id, data.content)
        return {"message": "Data ingested successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/rag/{user_id}/query", response_model=RAGResponse)
async def rag_query(user_id: str, query: RAGQuery):
    try:
        result = await RAGService.query(user_id, query.query)
        return RAGResponse(answer=result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/version")
def get_version():
    return {"version": "1.0.0"}  # Replace with your actual version number



@router.post("/test-constructor-flow", status_code=status.HTTP_200_OK)
async def test_constructor_flow():
    try:
        user_id = "test_user"
        async with GraphConstructor(user_id=user_id) as graph_constructor:
            context_retriever = GraphContextRetriever(graph_constructor.graph_ops)

            # Ensure vector index exists
            await graph_constructor.graph_ops.neo4j_manager.ensure_vector_index()

            # Clean up the graph first
            print("Cleaning graph for user:", user_id)
            await graph_constructor.clean_graph()
            # Recreate the vector index after cleaning
            await graph_constructor.graph_ops.neo4j_manager.ensure_vector_index()

            # # Process each sample statement
            # for statement in sample_statements:
            #     print(f"Processing text: {statement}")
            #     # Create UnstructuredData object
            #     data = UnstructuredData(title="Sample Statement", content=statement)
                
            #     # Process the unstructured data
            #     await graph_constructor.process_unstructured_data(data)

            #Process Astronaut Chat

            print(f"Processing text: {SPACE_SCHOOL_CHAT}")
            # Create UnstructuredData object
            data = UnstructuredData(title="Sample Statement", content=SPACE_SCHOOL_CHAT)
            
            # Process the unstructured data
            await graph_constructor.process_unstructured_data(data)

            
            # Retrieve and print the updated graph context
            print("Retrieving updated graph context...")
            context = await graph_constructor.get_graph_context("Technology")
            print("Updated graph context:", context)

            return {"status": "Graph updated successfully", "context": context}

    except Exception as e:
        print(f"Error during constructor test flow: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        print("Closing graph constructor...")
        await graph_constructor.close()


@router.post("/rag-query", status_code=status.HTTP_200_OK)
async def rag_query(query: str, user_id: str):
    try:
        rag = RAGInterface(user_id)
        response = await rag.query(query)
        return {"query": query, "response": response}
    except Exception as e:
        print(f"Error during RAG query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await rag.close()

@router.post("/rag-query-vector", status_code=status.HTTP_200_OK)
async def rag_query_vector(query: str, user_id: str):
    try:
        rag = RAGInterface(user_id)
        response = await rag.query_vector_only(query)
        return {"query": query, "response": response}
    except Exception as e:
        print(f"Error during vector-only RAG query: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await rag.close()