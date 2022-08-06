from django.urls import path
from . import views
from django.conf.urls.static import static
from djangoProject import settings


urlpatterns = [
    path('', views.root, name="home"),
    path('compiler/', views.compiler, name="compiler"),
    path('run/', views.run_code, name="run"),
    path('test/', views.test_code, name="test"),
    path('dcl/', views.dcl_check, name="dcl"),
    
    path('level_up/', views.level_up, name="level_up"),
    path('cd/<str:path>', views.cd, name="change_dir"),
    path('md/', views.md, name="make_dir"),
    path('rd/<str:folder_name>', views.rm, name="remove_dir"),

    path('fmd/<str:path>', views.file_md, name="make_file"),
    path('frd/<str:file_name>/<str:path>', views.file_rm, name="remove_file"),
    path('fedit/<str:file_name>/<str:path>', views.file_edit, name="edit_file"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
