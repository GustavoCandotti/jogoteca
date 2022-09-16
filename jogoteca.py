from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

app = Flask(__name__)  #faz referência ao proprio arquivo.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_pyfile('config.py')

db = SQLAlchemy(app) #instanciando nosso banco de dados. #(app) é o nosso argumento Flask.
csrf = CSRFProtect(app)   #Ele consiste em uma série de caracteres aleatórios,
# gerados a cada formulário a ser preenchido pelo usuário que é enviado pelo servidor.
bcrypt = Bcrypt(app)

from views_game import *
from views_user import *
#usou '*' para importar tudo.

if __name__ == '__main__':
    app.run(debug=True)
