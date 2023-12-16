from django.urls import path

from car import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("profile/<int:user_id>/", views.UserPurchasesView.as_view(), name="profile"),
    path("details/<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    path(
        "buy/<int:pk>/",
        views.BuyCarView.as_view(),
        {"template_name": "car_detail.html"},
        name="buy_car",
    ),
    path(
        "<int:brand_id>/", views.BrandBasedCarsView.as_view(), name="brand_based_cars"
    ),
]
