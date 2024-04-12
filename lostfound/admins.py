from lostfound import app, db, admin
from lostfound.models import Post, User

from flask_admin.contrib.sqla import ModelView

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))