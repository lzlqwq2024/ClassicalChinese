from django.urls import path,include,register_converter
from . import views

urlpatterns = [
    path('tologin/', views.tologin),
    path('article/<int:pagenum>/resetall/', views.article_reset_allstate),
    path('article/<int:pagenum>/resetpage/', views.article_reset_pagestate),
    path('article/<int:pagenum>/', views.article_index),
    path('article/<slug:snum>/', views.show_article),
    path('article/<slug:snum>/reply/<int:cid>/', views.comment_reply),
    path('article/<slug:snum>/riddle/', views.show_article_riddle),
    path('article/<slug:snum>/download/', views.download_article),
]
