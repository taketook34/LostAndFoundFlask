from lostfound import app, db, admin
from lostfound.models import Post, User
from flask_login import current_user
from flask_admin.contrib.sqla import ModelView

class MyAdmin(ModelView):

    def is_accessible(self):
        return current_user and current_user.is_staff


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))