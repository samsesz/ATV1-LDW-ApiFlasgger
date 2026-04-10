from pydantic import BaseModel

class DragonsSchema(BaseModel):
    id: int
    title: str
    description: str