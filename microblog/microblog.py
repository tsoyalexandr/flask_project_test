from app import app, db
from app.models import User, Post


# venv\Scripts\activate
# flask run
# flask shell

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
