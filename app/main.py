from fastapi import FastAPI
import app.models  # Importa todos os modelos!
from app.routers import auth, books

app = FastAPI()

app.include_router(auth.router,prefix="/auth", tags=["auth"])
app.include_router(books.router, prefix="/books", tags=["books"])