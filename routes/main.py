from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from db.database import SessionLocal, engine, Base
from modelos.models import Movie as mv
from pydantic import BaseModel
import logging

# Configuración de logging para SQLAlchemy
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

app = FastAPI()
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class movie_Schema(BaseModel):
    title: str
    description: str
    length: int
    director: str



@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    db = SessionLocal()
    movies = db.query(mv).all()
    movies_list = [{"id": movie.id, 
                    "title": movie.title, 
                    "Description": movie.description,
                    "length":movie.length,
                    "director":movie.director
                    } for movie in movies]
    if movies_list:
        return JSONResponse(content=movies_list)
    
    return JSONResponse(content="No movies found", status_code=404)

@app.get("/peliculas/{id}")
def get_movie_by_id(id: int, db: Session = Depends(get_db)):
    # Implementación para obtener detalles de una película
    pass

@app.post("/movies/")
def create_movie(movie: movie_Schema, db: Session = Depends(get_db)):
    new_movie = mv(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie