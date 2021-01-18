from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list_view.as_view()),
    path('detail/<int:id>', views.detail_page)
]