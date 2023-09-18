import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# DADOS SENSÍVEIS
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

# MEUS SEGREDOS
openai_key = os.getenv('OPENAI_KEY')
aws_secret = os.getenv('AWS_SECRET')
 
#MEU APP
print(f"Meu email: {email}")
print(f"Minha senha: {password}")
print(f"Minha Key Open AI: {openai_key}")
print(f"Minha AWS Key: {aws_secret}")