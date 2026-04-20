from fastapi import FastAPI
from app.routes import upload

#title 
app = FastAPI(title="NyayaAI Backend")

# Register routes
app.include_router(upload.router)