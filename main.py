from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Dataset(BaseModel):
    name: str
    description: str
    url: str
    keywords: list[str]
    license: str

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/v1/dataset/{dataset_id}", response_model=Dataset)
def get_dataset(dataset_id: int):
    dataset = fetch_dataset(dataset_id)  # replace with actual function to fetch dataset
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return {
        "@context": "https://schema.org/",
        "@type": "Dataset",
        "name": dataset.name,
        "description": dataset.description,
        "url": dataset.url,
        "keywords": dataset.keywords,
        "license": dataset.license,
    }

