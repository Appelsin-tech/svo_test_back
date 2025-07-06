from typing import List
from app.models import User, MessageOut

users: dict[int, User] = {
	1: User(id=1, name="Вася"),
	2: User(id=2, name="Маша"),
	3: User(id=3, name="Петя"),
}

messages: List[MessageOut] = []
message_id_counter: int = 1