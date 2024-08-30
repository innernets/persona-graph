import json
import openai
from typing import List, Tuple, Dict
from app.openai.prompts import GET_ENTITIES, GET_NODES_AND_RELATIONSHIPS
from app.utils.models import EntityExtractionResponse, NodesAndRelationshipsResponse
from app.config import config
import instructor
from instructor import OpenAISchema
from pydantic import Field
from app.utils.instructions_reader import INSTRUCTIONS

# Initialize the OpenAI client globally if not already set up elsewhere in your application
openai_client = openai.AsyncOpenAI(api_key=config.MACHINE_LEARNING.OPENAI_KEY)
client = instructor.from_openai(openai_client)

class Node(OpenAISchema):
    name: str
    perspective: str

class Relationship(OpenAISchema):
    source: str
    relation: str
    target: str

class GraphResponse(OpenAISchema):
    nodes: List[Node] = Field(..., description="List of nodes in the graph")
    relationships: List[Relationship] = Field(default_factory=list, description="List of relationships between nodes")

async def get_entities(text: str) -> Dict[str, List[str]]:
    """
    Extract entities from provided text using OpenAI's language model.
    """
    try:
        combined_instructions = f"App Objective: {INSTRUCTIONS}\n\nEntity Extraction Task: {GET_ENTITIES}"
        response = await openai_client.chat.completions.create(
            model='gpt-3.5-turbo-0125',
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": combined_instructions},
                {"role": "user", "content": text}
            ],
            temperature=0.5
        )
        # Extract entities from response, assuming the expected format is JSON
        content = response.choices[0].message.content
        print("Content: ", content)
        entities = json.loads(content)
        # print(f"Extracted entities: {entities['entities']}")
        return entities
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return {"entities": []}
    except Exception as e:
        print(f"Error while extracting entities: {e}")
        return {"entities": []}

async def get_nodes_and_relationships(entities: List[str], graph_context: str) -> GraphResponse:
    """
    Generate nodes and relationships based on the list of entities and existing graph context using OpenAI's language model.
    """
    entities_str = ', '.join(entities)
    combined_instructions = f"App Objective: {INSTRUCTIONS}\n\nEntity Extraction Task: {GET_ENTITIES}"
    try:
        response = await client.chat.completions.create(
            model='gpt-4-turbo',
            messages=[
                {"role": "system", "content": combined_instructions},
                {"role": "user", "content": f"Existing Graph Context:\n{graph_context}\n\nNew Entities: {entities_str}"}
                
            ],
            temperature=0.7,
            response_model=GraphResponse
        )
        nodes = response.nodes
        relationships = response.relationships
        print(f"Generated nodes: {nodes}")
        print(f"Generated relationships: {relationships}")
        return nodes, relationships
    except Exception as e:
        print(f"Error while generating nodes and relationships: {e}")
        return GraphResponse(nodes=[], relationships=[])

async def generate_response_with_context(query: str, context: str) -> str:
    prompt = f"""
    Given the following context from a knowledge graph and a query, provide a detailed answer:

    Context:
    {context}

    Query: {query}

    Please provide a comprehensive answer based on the given context:
    """

    response = await openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are a helpful assistant that answers queries about a user based on the provided context from their graph."},
            
        ]
    )
    return response.choices[0].message.content

# You can further use these functions in your application to update the graph or for other processes.