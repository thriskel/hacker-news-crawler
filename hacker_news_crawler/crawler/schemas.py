from pydantic import BaseModel


class PostUpdate(BaseModel):
    rank: int
    title: str
    title_length: int
    score: int
    comments: int
