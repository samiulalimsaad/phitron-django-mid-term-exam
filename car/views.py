from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .models import Brand, Car


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all()
        context["brand_based_cars"] = Car.objects.filter(brand__isnull=False)
        return context


class BrandBasedCarsView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        brand_id = self.kwargs["brand_id"]
        brand = get_object_or_404(Brand, pk=brand_id)
        print(brand_id, brand)
        context["brands"] = Brand.objects.all()
        context["brand_based_cars"] = Car.objects.filter(brand=brand)
        return context
