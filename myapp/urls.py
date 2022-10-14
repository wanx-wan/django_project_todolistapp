from django.urls import path
# from .views import index, profile
# from sciweb.views import *
from myapp import views

urlpatterns = [
    path('TodoList', views.AllList),
    path('AddList',views.AddList),
    path('editList/<int:id>', views.editList),
    path('UpdateList/<int:id>',views.UpdateList),
    path('DeleteList/<int:id>',views.DeleteList),
    path('SearchList',views.SearchList),
]
