from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Пример модели игры
class Game(BaseModel):
    id: int
    name: str
    version: str

# Временная "база данных"
games_db = [
    Game(id=1, name="Minecraft", version="1.20.1"),
    Game(id=2, name="Koala Adventure", version="0.1.0")
]

@app.get("/")
def root():
    return {"message": "Koala Launcher backend is running"}

@app.get("/api/games")
def get_games():
    return games_db

@app.get("/api/news")
def get_news():
    return [{"id": 1, "title": "Welcome to Koala Launcher!"}]

