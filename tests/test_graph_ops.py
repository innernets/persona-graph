import pytest
from app.graph.graph_ops import GraphOps
from app.utils.models import NodeModel, RelationshipModel

@pytest.mark.asyncio
async def test_add_node_with_embedding(neo4j_manager):
    graph_ops = GraphOps(neo4j_manager)
    node = NodeModel(name="Test Node", properties={"test": "property"})
    await graph_ops.add_node_with_embedding(node.name, "test_user", node.properties)
    
    # Verify node was added
    result = await graph_ops.get_node("Test Node", "test_user")
    assert result is not None
    assert result["name"] == "Test Node"
    assert result["properties"]["test"] == "property"

@pytest.mark.asyncio
async def test_add_relationship(neo4j_manager):
    graph_ops = GraphOps(neo4j_manager)
    await graph_ops.add_node_with_embedding("Source Node", "test_user", {})
    await graph_ops.add_node_with_embedding("Target Node", "test_user", {})
    
    relationship = RelationshipModel(source="Source Node", target="Target Node", relation="TEST_RELATION")
    await graph_ops.add_relationship(relationship.source, relationship.target, relationship.relation, "test_user")
    
    # Verify relationship was added
    result = await graph_ops.get_relationship("Source Node", "Target Node", "TEST_RELATION", "test_user")
    assert result is not None