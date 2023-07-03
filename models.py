from pydantic import BaseModel

class Dataset(BaseModel):
    name: str
    description: str
    url: str
    keywords: list[str]
    license: str
