from sqlalchemy.orm import Session

def process_message(message_body: str, sender: str, db: Session) -> str:
    message_lower = message_body.lower()

    if "horário" in message_lower:
        return "Nosso horário de atendimento é de segunda a sexta, das 6h às 00h e aos sabados das 7h as 15h."
    elif "planos" in message_lower:
        return "Temos planos a partir de R$ 50,00 mensais. Para saber mais, acesse nosso site."
    elif "endereço" in message_lower:
        return "Estamos localizados na Avenida Paulista, 1000, São Paulo - SP."
    else:
        return "Olá! Comos podemos lhe ajudar hoje?"