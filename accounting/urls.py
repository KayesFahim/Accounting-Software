from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from rest_framework import routers
from accounting import views
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('EmployeePortal.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
