from django.urls import path

from api.items.views import BuyItemView, GetItemView, ItemsListView

app_name = "items"

urlpatterns = [
    path("", ItemsListView.as_view(), name="items_list"),
    path("<int:id>/", GetItemView.as_view(), name="get_item"),
    path("bay/<int:id>/", BuyItemView.as_view(), name="buy_item"),
]
