from fastapi import APIRouter
from datetime import datetime, timezone
from app.models import MessageIn, MessageOut, User
from app import storage

router = APIRouter()

@router.get("/users", response_model=list[User])
async def get_users():
	return list(storage.users.values())

@router.get("/messages", response_model=list[MessageOut])
async def get_messages():
	return storage.messages

@router.post("/messages", response_model=MessageOut)
async def post_message(msg: MessageIn):
	user = storage.users.get(msg.sender_id)
	if not user:
		raise ValueError("User not found")

	new_msg = MessageOut(
		id=storage.message_id_counter,
		sender_id=user.id,
		sender_name=user.name,
		text=msg.text,
		sent_at=datetime.now(timezone.utc)
	)

	storage.message_id_counter += 1
	storage.messages.append(new_msg)
	return new_msg

@router.post("/messages/clear")
async def clear_messages():
	storage.messages.clear()
	storage.message_id_counter = 1
	return {"status": "cleared"}
