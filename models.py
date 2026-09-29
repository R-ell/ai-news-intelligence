from pydantic import BaseModel

class Article(BaseModel):
    title:str
    source:str
    url:str
    date_pub:str