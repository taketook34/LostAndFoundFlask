from lostfound import app
from lostfound.routes import HomeView, PostlistView, OnepostView, RegisterView, AddpostView, LoginView, LogoutView, ContactsView


app.add_url_rule("/", view_func=HomeView.as_view("home_page"), methods=['GET', 'POST'])
app.add_url_rule("/postlist", view_func=PostlistView.as_view("postlist_page"))
app.add_url_rule("/postlist/<post_id>", view_func=OnepostView.as_view("onepost_page"))
app.add_url_rule("/register", view_func=RegisterView.as_view("register_page"))
app.add_url_rule("/addpost", view_func=AddpostView.as_view("addpost_page"))
app.add_url_rule("/login", view_func=LoginView.as_view("login_page"))
app.add_url_rule("/logout", view_func=LogoutView.as_view("logout_page"))
app.add_url_rule("/contacts", view_func=ContactsView.as_view("contacts_page"))