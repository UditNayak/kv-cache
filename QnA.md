# QnA

## Why did I choose the python:3.11-slim version for this assignment?
- Python 3.11 is faster, especially for async tasks.
- The `slim` variant removes unnecessary libraries, reducing the image size (~20MB).
- Smaller images mean quicker build and deployment times.  

---

## Why do we need Uvicorn?
- **ASGI server:** FastAPI relies on an ASGI server like Uvicorn to handle HTTP and WebSocket requests asynchronously.
- It helps the app handle multiple requests at the same time.
