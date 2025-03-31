from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.lru_cache import LRUCache

app = FastAPI()

cache = LRUCache()

class KeyValuePair(BaseModel):
    key: str
    value: str

@app.post("/put")
def put_item(item: KeyValuePair):
    if len(item.key) > 256 or len(item.value) > 256:
        return {"status": "ERROR", "message": "Key or value exceeds 256 characters."}
    try:
        cache.put(item.key, item.value)
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}
    return {"status": "OK", "message": "Key inserted/updated successfully."}

@app.get("/get")
def get_item(key: str):
    try:
        value = cache.get(key)
        if value is None:
            return {"status": "ERROR", "message": "Key not found."}
        return {"status": "OK", "key": key, "value": value}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}