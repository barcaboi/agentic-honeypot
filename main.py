from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os

from scam_detector import detect_scam
from agent import honey_pot_agent
from extractor import extract_intel

app = FastAPI(title="Agentic Honey-Pot API")

API_KEY = os.getenv("API_KEY", "test123")

class Message(BaseModel):
    role: str
    content: str

class ScamRequest(BaseModel):
    conversation_id: str
    message: str
    conversation_history: List[Message] = []
    timestamp: str

def verify_api_key(auth: Optional[str]):
    if auth != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

@app.post("/scam-detect")
def scam_detect(
    data: ScamRequest,
    authorization: Optional[str] = Header(None)
):
    verify_api_key(authorization)

    detection = detect_scam(data.message)

    response = {
        "conversation_id": data.conversation_id,
        "scam_detected": detection["is_scam"],
        "confidence_score": detection["confidence"],
        "agent_engaged": False,
        "engagement_metrics": {},
        "extracted_intelligence": {},
        "agent_reply": ""
    }

    if detection["is_scam"]:
        agent_reply = honey_pot_agent(
            data.conversation_history,
            data.message
        )

        intel = extract_intel(data.message)

        response.update({
            "agent_engaged": True,
            "engagement_metrics": {
                "total_turns": len(data.conversation_history) + 1,
                "engagement_duration_seconds": 120
            },
            "extracted_intelligence": intel,
            "agent_reply": agent_reply
        })

    return response

