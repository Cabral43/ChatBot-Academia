from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_whatsapp_webhook():
    response = client.post(
        "/webhook",
        data={"Body": "Horário", "From": "whatsapp:+5541999808460"}
    )
    assert response.status_code == 200
    assert "Nosso horário de atendimento é de segunda a sexta, das 6h às 00h e aos sabados das 7h as 15h." in response.text
