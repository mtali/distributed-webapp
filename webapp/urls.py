from django.contrib import admin
from django.urls import path, include

from customers.api.views import CustomersListApiView
from hubs.api.views import DeviceInfoApiView
from packs.api.views import PacksListApiView
from sales.api.views import MembershipListApiView
from staffs.api.views import StaffsListApiView
from webhooks.api.views import WebhookApiView
from . import views

admin.site.site_header = "WebApp Admin"

urlpatterns = [
    path('api/v1/memberships/', MembershipListApiView.as_view(), name='memberships-list'),
    path('api/v1/customers/', CustomersListApiView.as_view(), name='customers-list'),
    path('api/v1/device_info/', DeviceInfoApiView.as_view(), name='device-info'),
    path('api/v1/staffs/', StaffsListApiView.as_view(), name='staff-list'),
    path('api/v1/packs/', PacksListApiView.as_view(), name='pack-list'),
    path('api/v1/webhooks/', WebhookApiView.as_view(), name='webhooks'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/docs', views.APIRootView.as_view()),
    path('', admin.site.urls),
]
