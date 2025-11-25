from fastapi import FastAPI
from api.router import router

app = FastAPI(
    title="ML Enhanced Password Security API",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Password Security API is live!"}
