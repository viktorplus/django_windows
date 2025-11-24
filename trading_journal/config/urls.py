from django.contrib import admin
from django.urls import path
from journal.views import trades_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", trades_list, name="trades_list"),
]
