# Atividade de DevOps (Criando Pipeline de CI/CD com Github Actions)

## Como rodar localmente

**Pré-requisitos**
* python 3.12.3
* git

**Faça o clone do projeto usando o comando**
* `git clone https://github.com/alexandremariano4/exercicio-github-actions.git`

**Entre na pasta do projeto e use crie um novo ambiente virtual**
* `python -m venv .venv`

**Ao abrir o ambiente virtual instale o poetry, que foi usado como gerenciador de dependências no projeto**
* `pip install poetry`

**Instale as dependências com o poetry usando**
* `poetry install --only main`

**Ao instalar as dependências, inicie a aplicação em um terminal (no caso de windows) usando o comando**
* `flask --app main run `
**Caso não funcione assim, tente:** 
* `python -m flask --app main run`
**🚨Garanta que esteja no ambiente virtual!**

**Caso esteja no Linux e queira fazer tudo no mesmo terminal, use o gunicorn para executar o servidor e iniciar a aplicação com o comando**
* `gunicorn -b 127.0.0.1:5000 main:app`

**Abra outro terminal e execute o comando** `pytest` **na pasta principal do projeto para executar os testes**

