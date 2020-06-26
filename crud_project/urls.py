from django.contrib import admin
from django.urls import path
from crud_app import views
app_name='crud_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add_show,name='add_show'),
    path('delete-student/<int:id>/',views.delete_student,name='delete_student'),
    path('Update-Data/<int:id>/', views.update_data,name='update_data'),
]
