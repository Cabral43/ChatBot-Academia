from fastapi import  APIRouter, Request, Response, Depends
from sqlalchemy.orm import Session
from twilio.twiml.messaging_response import MessagingResponse
from app.services.messaging import process_message
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/webhook")
async def whatsapp_webhook(request: Request, db:  Session = Depends(get_db)):
    form = await request.form()
    message_body = form.get("Body")
    sender = form.get("From")

    response_text = process_message(message_body, sender, db)

    resp = MessagingResponse()
    resp.message(response_text)

    return Response(content=str(resp), media_type="application/xml")