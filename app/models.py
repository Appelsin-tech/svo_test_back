from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
	id: int
	name: str

class MessageIn(BaseModel):
	sender_id: int
	text: str

class MessageOut(BaseModel):
	id: int
	sender_id: int
	sender_name: str
	text: str
	sent_at: datetime
