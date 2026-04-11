from pydantic import BaseModel

class DragonsSchema(BaseModel):
    title: str
    description: str