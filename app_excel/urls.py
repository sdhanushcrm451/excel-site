from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.start_session, name='start_session'),
    path('add-values/', views.add_values, name='add_values'),
    path('end-session/', views.end_session, name='end_session'),
    path('download-excel/', views.download_excel, name='download_excel'),
    path('value-added/', views.value_added, name='value_added'), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)