from django.urls import include, path


app_name = "api"

urlpatterns = [path("items/", include("api.items.urls", namespace="items")),]
