from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    app.config.from_object('app.config.TestingConfig')

    from .auth import auth_page
    app.register_blueprint(auth_page, url_prefix='/auth')

    @app.route('/')
    def index_page():
        return render_template('index.html')

    return app