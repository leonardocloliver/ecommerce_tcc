import os

def get_postgres_uri():
    host = os.getenv("POSTGRES_HOST", "db") 
    port = os.getenv("POSTGRES_PORT", 5432) 
    password = os.getenv("POSTGRES_PASSWORD", "admin")
    user = os.getenv("POSTGRES_USER", "admin")
    db_name = os.getenv("POSTGRES_DB", "ecommerce")
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"