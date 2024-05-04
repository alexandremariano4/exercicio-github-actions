from flask import Flask,request

app = Flask(__name__)


@app.route("/")
def index():
    return "Home Page"

@app.route('/users/',methods=['GET'])
def show_subpath():
    return {
        'usuarios': [
            {'1':
                {
                    'nome': 'Alexandre',
                    'telefone': '31945464616',
                    'endereco': 'Rua dos testes',
                    'cidade': 'Belo Horizonte'
                }
            },
            {'2':
                {
                    'nome': 'Caroline',
                    'telefone': '339416489',
                    'endereco': 'Rua dos arrobas',
                    'cidade': 'São Paulo'
                }
            },
            {'3':
                {
                    'nome': 'Erika',
                    'telefone': '11994621994',
                    'endereco': 'Rua um',
                    'cidade': 'Rio de janeiro'
                }
            },

        ]
    }
