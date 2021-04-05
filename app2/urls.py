from django.urls import path
from app2 import views
app_name = 'app2'

urlpatterns = [
    path('index2',views.index2,name = 'index'),
    path('sample2/',views.sam2,name = 'sample2'),
    path('sample_app2/',views.ren2,name = 'sample_app2'),

]