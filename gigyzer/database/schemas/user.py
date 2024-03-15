from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserModel(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    username: str
    user_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


__all__ = ["UserModel"]
