from pydantic import BaseModel

class CharactersSchema(BaseModel):
    title: str
    description: str