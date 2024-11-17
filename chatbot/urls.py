from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name='chatbot'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
]

# 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
# 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
