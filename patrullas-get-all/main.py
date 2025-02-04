from fastapi import FastAPI
from routers.router import router as patrulla_router
from models.db import engine
from sqlalchemy.sql import text

app = FastAPI(title="Patrullas API")

# Registrar las rutas de patrullas
app.include_router(patrulla_router, prefix="/api", tags=["patrullas"])

@app.on_event("startup")
async def startup():
    """
    Verifica la conexión a la base de datos al iniciar.
    """
    async with engine.begin() as conn:
        await conn.execute(text("SELECT 1"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
