from django.urls import path
from app import views
app_name = 'app'

urlpatterns = [
    path('index',views.index,name = 'index'),
    path('sample1/',views.sam1,name = 'sample1'),
    path('sample_app1/',views.ren1,name = 'sample_app1'),

]
