from pydantic import BaseModel

class CharactersSchema(BaseModel):
    id: int
    title: str
    description: str