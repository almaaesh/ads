from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Count, F
from django.shortcuts import render
from django.utils import translation
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView
from .models import Product, Category, Country


class ProductListView(ListView):
    model = Product
    template_name = 'ads/home.html'
    context_object_name = 'list_ads'
    paginate_by = 10

    def get_queryset(self):
        lang = translation.get_language()
        if lang == "ar":
            return Product.objects.filter(Q(title_ar__isnull=False))
        elif lang == 'en':
            return Product.objects.filter(Q(title_en__isnull=False))
        else:
            return Product.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.get_categories()
        return context


class ProductByCountryListView(ProductListView):
    def get_queryset(self):
        self.country = Country.get_country_by_slug(self.kwargs['country_slug'])
        products = Product.get_country_products(self.country)
        return products


class ProuctByCategoryListView(ProductListView):
    def get_queryset(self):
        self.category = Category.get_category_by_slug(self.kwargs['category_slug'])
        products = Product.get_category_products(self.category)
        return products


class ProuctByCountryCategoryListView(ProductListView):
    def get_queryset(self):
        self.country = Country.get_country_by_slug(self.kwargs['country_slug'])
        self.category = Category.get_category_by_slug(self.kwargs['category_slug'])
        products = Product.get_country_category_products(self.country, self.category)
        return products


class ProductDetailView(DetailView):
    model = Product
    template_name = 'ads/product-detail.html'

    def get_object(self):
        product = super().get_object()
        print(product.view, 'Breack')
        product.view += 1
        product.save()
        # Todo: why increment by 2?! and use cache every 30 second
        return product

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        # context['visitors'] = Product.increase_visit_count(commit=True)
        return context


class UserPostListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'ads/user_post_list.html'

    def get_queryset(self):
        return Product.objects.filter(user=self.request.user)
