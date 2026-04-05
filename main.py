from fastapi import FastAPI
from app.routes import user_routes, record_routes, dashboard_routes

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)

@app.get("/")
def root():
    return {"message": "Finance Dashboard API Running"}