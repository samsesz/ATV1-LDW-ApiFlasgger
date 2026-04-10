from pydantic import BaseModel

class HousesSchema(BaseModel):
    id: int
    title: str
    description: str