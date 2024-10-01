ChatBot da Academia
ChatBot da Academia é um chatbot desenvolvido em Python que integra o FastAPI com o WhatsApp via Twilio para auxiliar no atendimento de clientes de uma academia. O bot responde a perguntas frequentes dos clientes, como horários de funcionamento, planos disponíveis e localização.

Índice
Pré-requisitos
Instalação
Configuração
Executando a Aplicação
Testes
Estrutura do Projeto
Tecnologias Utilizadas
Contribuição
Licença
Contato
Pré-requisitos
Python 3.11.8 instalado
Conta no Twilio com acesso ao Sandbox do WhatsApp
ngrok (para expor o servidor local)
Instalação
Clone o repositório:

bash
Copiar código
git clone https://github.com/SEU_USUARIO/ChatBot-Academia.git
cd ChatBot-Academia
Crie e ative o ambiente virtual:

No Windows:

bash
Copiar código
python -m venv .venv
.venv\Scripts\activate
No macOS/Linux:

bash
Copiar código
python3 -m venv .venv
source .venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Configuração
Crie o arquivo .env na raiz do projeto e configure as variáveis de ambiente:

env
Copiar código
DATABASE_URL=sqlite:///./test.db
TWILIO_ACCOUNT_SID=SEU_ACCOUNT_SID
TWILIO_AUTH_TOKEN=SEU_AUTH_TOKEN
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886  # Número padrão do Sandbox do Twilio
Substitua SEU_ACCOUNT_SID e SEU_AUTH_TOKEN pelas suas credenciais do Twilio.
Importante: Nunca compartilhe este arquivo publicamente.
Configure o banco de dados:

Execute as migrações para criar o banco de dados SQLite:

bash
Copiar código
alembic upgrade head
Executando a Aplicação
Inicie o servidor FastAPI com o Uvicorn:

bash
Copiar código
uvicorn app.main:app --reload
O servidor estará rodando em http://127.0.0.1:8000.

Exponha o servidor local usando o ngrok:

Em outro terminal, execute:

bash
Copiar código
ngrok http 8000
Copie o URL fornecido pelo ngrok (por exemplo, https://abcd1234.ngrok.io).

Configure o webhook no Twilio:

Acesse o painel do Twilio e vá para o Sandbox do WhatsApp.

Em "When a message comes in", insira o URL do ngrok com o endpoint /webhook:

bash
Copiar código
https://abcd1234.ngrok.io/webhook
Salve as configurações.

Teste o chatbot:

Envie uma mensagem para o número do Sandbox do WhatsApp seguindo as instruções do Twilio.
Interaja com o chatbot enviando mensagens como "Qual é o horário?" ou "Quais são os planos?".
Testes
Para executar os testes automatizados, use:

bash
Copiar código
pytest
Os testes estão localizados na pasta tests/ e verificam se as respostas do chatbot estão corretas.

Estrutura do Projeto
markdown
Copiar código
ChatBot-Academia/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── user.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   └── services/
│       ├── __init__.py
│       └── messaging.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── alembic/
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
└── ...
Tecnologias Utilizadas
Python 3.11.8
FastAPI: Framework web para construção de APIs.
Uvicorn: Servidor ASGI para executar a aplicação FastAPI.
SQLAlchemy: ORM para interagir com o banco de dados.
Alembic: Gerenciamento de migrações do banco de dados.
Twilio API: Integração com o WhatsApp.
ngrok: Exposição do servidor local para a internet.
pytest: Framework de testes.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias, correções de bugs ou novas funcionalidades.

Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/nova-feature).
Commit suas alterações (git commit -m 'Adiciona nova feature').
Envie para a branch (git push origin feature/nova-feature).
Abra um Pull Request.
Licença
Este projeto está licenciado sob a MIT License.

Contato
Nome: Carlos Cabral
Email: cabralc43@gmail.com
LinkedIn: https://github.com/Cabral43
