import os 

def get_backend_url():
    backend_url = os.getenv("BACKEND_URL", "http://backend:8000")
    return backend_url