from pydantic import BaseModel

class HousesSchema(BaseModel):
    title: str
    description: str