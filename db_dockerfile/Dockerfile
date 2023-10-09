# Imagem base do MySQL
FROM mysql:latest

# Arquivos SQL para o diretório de inicialização
COPY ./script.sql/ /docker-entrypoint-initdb.d/

# Exponha a porta padrão do MySQL (3306)
EXPOSE 3306

# Comando de inicialização do MySQL
CMD ["mysqld"]
