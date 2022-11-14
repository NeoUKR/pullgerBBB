from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('pullgerAuthJWT.urls')),
    path('pullgerTB/api/', include('djTaskBrocker.urls')),
    path('pullgerDS/api/', include('pullgerDataSynchronization__REST.urls')),
    path('pullgerAM/api/', include('pullgerAccountManager__REST.urls')),
    path('pullgerMSM/api/', include('pullgerMultiSessionManager__REST.urls')),
    path('pullgerR/org_bbb/api/', include('pullgerReflection.org__bbb__REST.urls')),
]
