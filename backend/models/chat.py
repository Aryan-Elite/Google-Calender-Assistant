from pydantic import BaseModel
from typing import Optional, Dict, Any

class ChatRequest(BaseModel):
    user_email: str
    user_message: str
    calendar_id: str
    conversation_context: Optional[Dict[str, Any]] = {}  # Track appointment details

class ChatResponse(BaseModel):
    answer: str
    context: Optional[Dict[str, Any]] = {}  # Return updated context
    requires_confirmation: bool = False  # Flag if confirmation needed