from pydantic import BaseModel


class PostUpdate(BaseModel):
    rank: int
    title: str
    title_length: str
    score: int
    comments: int
