
from flask import Flask
from config import Config

from controllers.home_controller import home_bp
from controllers.livros_controller import livros_bp
from controllers.conteudo_controller import conteudo_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(home_bp)
    app.register_blueprint(livros_bp)
    app.register_blueprint(conteudo_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
