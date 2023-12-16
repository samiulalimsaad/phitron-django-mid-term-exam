from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import FormView, UpdateView

from car.form import BuyCarForm, CommentForm, UserEditForm
from comment.models import Comment

from .models import Brand, Buy, Car


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


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = Comment.objects.filter(car=self.object)
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            car = self.get_object()
            Comment.objects.create(
                user=request.user, car=car, text=form.cleaned_data["text"]
            )
            return redirect("car_detail", pk=car.pk)
        else:
            # Handle invalid form submission
            context = self.get_context_data()
            context["form"] = form
            return self.render_to_response(context)


class BuyCarView(LoginRequiredMixin, FormView):
    template_name = (
        "car_detail.html"  # You can keep this template or use a separate one
    )
    form_class = BuyCarForm

    def form_valid(self, form):
        car_id = self.kwargs["pk"]
        car = Car.objects.get(pk=car_id)

        # Perform the buying logic, create a Buy instance, etc.
        Buy.objects.create(user=self.request.user, car=car)

        messages.success(self.request, f"You have successfully bought {car.name}!")
        return redirect("car_detail", pk=car_id)

    def form_invalid(self, form):
        car_id = self.kwargs["pk"]
        messages.error(
            self.request, "Invalid form submission. Please correct the errors."
        )
        return redirect("car_detail", pk=car_id)


class UserPurchasesView(ListView):
    template_name = "profile.html"  # Create this template
    context_object_name = "purchases"
    model = Buy

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = User.objects.get(pk=user_id)
        return Buy.objects.filter(user=user).order_by("-purchase_date")


class UserEditView(UpdateView):
    model = User
    form_class = UserEditForm
    template_name = "user_edit.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        return self.request.user
