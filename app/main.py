from fastapi import FastAPI
from app.api.routes.auth import router as auth_router
from app.api.routes import profile
from app.db import init_db
from contextlib import asynccontextmanager
from app.schemas import Band, Bands, Genre

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield
    
app = FastAPI(lifespan=lifespan)

Bands = [
    {"id": 1, "name": "Nirvana", "genre": "Grunge"},
    {"id": 2, "name": "Pink Floyd", "genre": "Progressive Rock"},
    {"id": 3, "name": "Radiohead", "genre": "Alternative"},
    {"id": 4, "name": "Led Zeppelin", "genre": "Rock"},
]
@app.get("/")
def home():
    return {"message" :"Welcome to the FastAPI application!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/bands")
def get_bands() -> list[Band]:
    return [
       Band(**band) for band in Bands
    ]


# using path parameters
@app.get("/bands/{band_id}")
def get_band(band_id: int) -> Band:
    for band in Bands:
        if band["id"] == band_id:
            return band
    return {"error": "Band not found"}, 404

# kind of like query parameters
@app.get("/bands/genre")
def get_bands_by_genre(genre: Genre) -> list[dict]:
    filtered_bands = [band for band in Bands if band["genre"].lower() == genre.value.lower()]
    if not filtered_bands:
        return {"error": "No bands found for this genre"}, 404
    return filtered_bands

# kind of path parameters
@app.get("/bands/genre/{genre}")
def get_bands_by_genre_path(genre: Genre) -> list[dict]:
    filtered_bands = [band for band in Bands if band["genre"].lower() == genre.value.lower()]
    if not filtered_bands:
        return {"error": "No bands found for this genre"}, 404
    return filtered_bands

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(profile.router, prefix="/profile", tags=["Profile"])
