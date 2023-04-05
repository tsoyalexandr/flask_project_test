from app import app, db
from app.models import User, Post


# venv\Scripts\activate
# flask run
# flask shell
# users = User.query.all()
# users
# set FLASK_DEBUG=0

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
