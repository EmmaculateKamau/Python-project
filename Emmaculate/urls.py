from  django.urls import path
from .import views

app_name='Emmaculate'

urlpatterns=[
    #after path the next thing is a function
    #class based views
   path('',views.MemberListView.as_view(),name='index'),
   path('add-member',views.MemberCreateView.as_view(),name='add-member'),
   #<int:pk>is the id
   path('<int:pk>/update',views.MemberUpdateView.as_view(),name='update-member'),
   path('<int:pk>/delete',views.MemberDeleteView.as_view(),name='delete-member'),
]