from django.urls import path
from .import views

urlpatterns = [
    # path(url, function)
    path('',views.article_list),
]
