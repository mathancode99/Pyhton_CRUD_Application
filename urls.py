from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('home',home,name='home'),
    path('sd',Studentdetails,name='studentdetails'),
    path('sd/del/<int:id>/',deldata,name="del_info"),
    path('sd/update/<int:id>/',updatedata,name="update_info"),

]