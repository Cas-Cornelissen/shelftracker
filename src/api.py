from fastapi import FastAPI, HTTPException
import requests

api = FastAPI()

@api.get("/test")
async def root():
    return {"message": "Hello World"}

@api.get("/books/{isbn}")
async def get_book(isbn: str):
    response = requests.get(f'https://openlibrary.org/isbn/{isbn}.json')
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Book not found")
    return response.json()

@api.get("/books/client/{isbn}")
async def get_book(isbn: str):
    response = requests.get(f'https://openlibrary.org/isbn/{isbn}.json')
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Book not found")
    data = response.json()
    return {"title": data.get("title"), "publish_date": data.get("publish_date")}
