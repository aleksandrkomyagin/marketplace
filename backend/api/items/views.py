import stripe

from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.views.generic import TemplateView

from rest_framework import status, views
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from items.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemsListView(TemplateView):
    permission_classes = (AllowAny, )
    template_name = "items/index.html"

    def get_context_data(self, **kwargs):
        context = super(ItemsListView, self).get_context_data(**kwargs)
        context["items"] = Item.objects.all()
        return context


class GetItemView(TemplateView):
    permission_classes = (AllowAny, )
    template_name = "items/item.html"

    def get_context_data(self, **kwargs):
        context = super(GetItemView, self).get_context_data(**kwargs)
        id = self.kwargs.get("id")
        context["item"] = Item.objects.get(id=id)
        context["STRIPE_PUBLIC_KEY"] = settings.STRIPE_PUBLIC_KEY
        return context


class BuyItemView(views.APIView):
    permission_classes = (AllowAny, )

    def get(self, request, id):
        try:
            item = Item.objects.get(id=id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        site = get_current_site(request)
        protocol = "https:/" if request.is_secure() else "http:/"

        checkout_session = stripe.checkout.Session.create(
            settings.STRIPE_SECRET_KEY,
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "usd",
                        "product_data": {"name": item.name,},
                        "unit_amount": item.price * 100,
                        },
                    "quantity": 1,
            },
            ],
            mode="payment",
            metadata={
                "id": item.id
            },
            success_url="/".join((protocol, site.domain, "success")),
            cancel_url="/".join((protocol, site.domain, "cancel")),
        )

        return JsonResponse({
            "id": checkout_session.id
        })
