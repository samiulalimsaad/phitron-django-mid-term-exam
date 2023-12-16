from django.urls import path

from car import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path(
        "<int:brand_id>/", views.BrandBasedCarsView.as_view(), name="brand_based_cars"
    ),
]
