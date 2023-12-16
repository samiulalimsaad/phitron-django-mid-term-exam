from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView

from car.form import CommentForm
from comment.models import Comment

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
