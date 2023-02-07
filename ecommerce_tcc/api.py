import fastapi as _fastapi

app = _fastapi.FastAPI()

@app.get("/v1/api/products/")
async def create_product():
    return "Hello world"
