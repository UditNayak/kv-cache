from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory key-value cache
cache = {}

class KeyValuePair(BaseModel):
    key: str
    value: str

@app.post("/put")
def put_item(item: KeyValuePair):
    if len(item.key) > 256 or len(item.value) > 256:
        raise HTTPException(status_code=400, detail="Key or value exceeds 256 characters")
    cache[item.key] = item.value
    return {"status": "OK", "message": "Key inserted/updated successfully."}

@app.get("/get")
def get_item(key: str):
    try:
        if key in cache:
            return {"status": "OK", "key": key, "value": cache[key]}
        return {"status": "ERROR", "message": "Key not found."}
    except Exception as e:
        return {"status": "ERROR", "message": f"Error: {str(e)}"}