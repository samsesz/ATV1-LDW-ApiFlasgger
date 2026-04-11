from pydantic import BaseModel

class SwordsSchema(BaseModel):
    title: str
    description: str