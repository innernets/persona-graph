from app.graph.constructor import GraphConstructor
from app.utils.models import UnstructuredData

class IngestService:
    @staticmethod
    async def ingest_data(user_id: str, content: str):
        async with GraphConstructor(user_id) as constructor:
            data = UnstructuredData(title="Ingested Data", content=content)
            await constructor.process_unstructured_data(data)
        
        return {"message": "Data ingested successfully"}