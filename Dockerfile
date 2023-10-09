# Imagem Base
FROM python:3.10

# Diretório de trabalho
WORKDIR /app

# Cópia dos arquivos da aplicação
COPY . .

# Instalação de dependências
RUN pip3 install -r requirements.txt

# Comando para executar aplicação
CMD ["python3", "run.py"]
