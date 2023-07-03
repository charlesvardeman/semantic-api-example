# Path: main.py
from fastapi import FastAPI
from models import Dataset, Identifier

app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "Hello, World!"}

# Path: main.py
@app.get("/dataset")
def read_dataset():
    return {"message": "Hello, Dataset!"}


@app.get("/dataset/{dataset_id}")
def get_dataset(dataset_id: int):
    # For now, return a hard-coded dataset
    dataset = Dataset(
        name="Test Dataset",
        description="This is a test dataset",
        url="http://example.com/datasets/1",
        sameAs="http://example.com/datasets/1",
        version="1.0",
        isAccessibleForFree=True,
        keywords=["test", "dataset"],
        identifier=Identifier(identifier="doi:10.1000/test"),
        variableMeasured="Test variable"
    )
    return {"@context": "https://schema.org/", "@type": "Dataset", **dataset.dict()}



# Create a main function that runs the application using uvicorn.
# Path: main.py
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
