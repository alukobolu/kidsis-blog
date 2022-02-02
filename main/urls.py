from django.urls import path
from .views import Home,Response,Dashboard,ListResponses,MakeTopics,EditTopics,DeleteTopic

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('home/<id>/', Response.as_view(), name='respond'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'), 
    path('make/', MakeTopics.as_view(), name='make'),
    path('edit/<id>/', EditTopics.as_view(), name='edit'),
    path('delete/<id>/', DeleteTopic.as_view(), name='delete'),
    path('dashboard/<id>/', ListResponses.as_view(), name='response_list'), 
] 
