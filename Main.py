# main.py
from fastapi import FastAPI, WebSocket, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List, Optional
import jwt
import asyncio
import uvicorn
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

# Configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
MONGODB_URL = "mongodb://localhost:27017"

app = FastAPI(title="Task Management API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
client = AsyncIOMotorClient(MONGODB_URL)
db = client.taskmanager

# Models
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    status: str = "pending"
    assigned_to: Optional[str] = None
    created_by: str
    created_at: datetime = datetime.now()

class TokenData(BaseModel):
    username: Optional[str] = None

# WebSocket connection manager
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            await connection.send_json(message)

manager = ConnectionManager()
