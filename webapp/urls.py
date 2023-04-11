from django.contrib import admin
from django.urls import path, include

from sales.api.views import MembershipListApiView
from . import views

urlpatterns = [
    path('api/v1/memberships/', MembershipListApiView.as_view(), name='memberships-list'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/docs', views.APIRootView.as_view()),
    path('', admin.site.urls),
]
