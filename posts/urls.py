from django.urls import path
from .views import new, create, show

app_name = "posts"
urlpatterns = [
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:post_id>/', show, name="show"),
]