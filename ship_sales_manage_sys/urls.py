from django.urls import path

from . import views

app_name = "ship_sales_manage_sys"

urlpatterns = [
    path("", views.index, name="index"),
    path("ai",views.AI_view, name="ai")
]