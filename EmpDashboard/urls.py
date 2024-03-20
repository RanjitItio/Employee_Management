from django.contrib import admin
from django.urls import path, include
from EmpDashboard import settings
from django.conf.urls.static import static
from django.contrib.admin.options import ModelAdmin



urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('emp/', include('Employees.urls')),
]


if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  