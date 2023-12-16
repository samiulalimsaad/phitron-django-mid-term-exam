from django.urls import path

from car import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("details/<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    path(
        "<int:brand_id>/", views.BrandBasedCarsView.as_view(), name="brand_based_cars"
    ),
]
