from pydantic import BaseModel

class SwordsSchema(BaseModel):
    id: int
    title: str
    description: str