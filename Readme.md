# Key-Value Cache Service  

## Overview  
This project implements an in-memory key-value cache service using FastAPI. The service provides two APIs:  
- **`POST /put`** – Insert or update key-value pairs.  
- **`GET /get`** – Retrieve values by key.  

The service is containerized using Docker and runs on port **7171**.  

## Folder Structure  
```plaintext
kv-cache/
├── app/
│   ├── main.py
├── images/
├── Dockerfile
├── requirements.txt
├── QnA.md
└── README.md
```

## Setup Instructions 
1. Make sure you have Docker and Docker Compose installed
2. Run the following command to build the Docker image:
```sh
docker build -t kv-cache .
```
3. Execute the following to start the container:
```sh
docker run -p 7171:7171 kv-cache
```

## API Usage 
### 1. Insert/Update a Key-Value Pair 
- **Endpoint:** `POST /put`  
- **Request Body:**  
```json
  {
      "key": "Udit",
      "value": "34"
  }
```
- **cURL Command:**
```sh
curl --location 'http://localhost:7171/put' \
--header 'Content-Type: application/json' \
--data '{
    "key": "Udit",
    "value": "34"
}'
```
- **Example Response:**
![Post API](./images/post_api.png)

### 2. Get a Value by Key
- **Endpoint:** `GET /get`
- **Query Parameter:** `key`
- **cURL Command:**
```
curl --location 'http://localhost:7171/get?key=Udit'
```
#### Cache-Hit
![Cache Hit](./images/cache_hit.png)
#### Cache-Miss
![Cache Miss](./images/cache_miss.png)


### To-Do:
- Implement Cache Eviction (LRU).
- Use Loose Coupling for Cache Eviction to allow easy future changes (Open/Closed Principle).
- Optimize for high concurrency (Use Locks).
- Use Multithreading for low latency.
- Implement Docker Live Reload for faster development.
- Create a separate folder for schemas (request + response) [Better folder structure].
