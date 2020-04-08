from django.core.validators import RegexValidator
from django.db import models
from django.db.models import Q
from django.urls import reverse
from django.utils import translation, timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from .media_handlers import *
from .validators import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                verbose_name=_('Username'),
                                related_name='profiles',
                                blank=False,
                                null=True,
                                )
    display_name = models.CharField(verbose_name=_('Display Name'), null=True, blank=True, max_length=50)
    biography = models.TextField(verbose_name=_('Biography'), null=True, blank=True)
    GENDER_CHOICES = (
        ('', _("---")),
        ('M', _('Male')),
        ('F', _('Female'))
    )
    gender = models.CharField(verbose_name=_('Gender'), choices=GENDER_CHOICES, max_length=10, default='', null=True,
                              blank=True)
    mobile = models.CharField(verbose_name=_('Mobile'), null=True, blank=True, max_length=12)
    banck_account = models.CharField(verbose_name=_('Bank Account'), null=True, blank=True, max_length=500)
    website = models.URLField(verbose_name=_('Website'), null=True, blank=True, max_length=100)
    twitter = models.CharField(verbose_name=_('Twitter'), null=True, blank=True, max_length=100)
    facebook = models.CharField(verbose_name=_('Facebook'), null=True, blank=True, max_length=100)
    linkedin = models.CharField(verbose_name=_('Linkedin'), null=True, blank=True, max_length=100)
    youtube = models.CharField(verbose_name=_('Youtube'), null=True, blank=True, max_length=100)
    google_plus = models.CharField(verbose_name=_('Google Plus'), null=True, blank=True, max_length=100)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL,
                                verbose_name=_('Default country'), null=True, blank=True)

    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, verbose_name=_('Country'), null=True, blank=True)
    # photo = models.FileField(
    #     null=True,
    #     blank=True,
    #     max_length=100,
    #     verbose_name=_('Your Picture'),
    #     upload_to=upload_location_picture,
    #     validators=[validate_image_extension],
    #     help_text=_('Allowed formats: jpg, png, bmp, gif.')
    # )

    def __str__(self):
        return str(self.user)

    # USERNAME_FIELD = 'user'
    # REQUIRED_FIELDS = ['user']

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     try:
    #         instance.user.save()
    #     except:
    #         user = Profile.objects.create(user=instance)

    # def __init__(self, *args, **kwargs):
    #     super(Profile, self).__init__(*args, **kwargs)
    #     self._meta.get_field('username').verbose_name = _('Username')

    # class Meta:
    #     verbose_name = "user"
    #     verbose_name_plural = "Users: Change Password"


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products', blank=True, null=True)
    title_ar = models.CharField(verbose_name=_('Title Ar'), max_length=250, null=True, blank=True, )
    title_en = models.CharField(verbose_name=_('Title En'), max_length=250, null=True, blank=True, )
    country = models.ForeignKey('Country', on_delete=models.CASCADE, blank=True, null=True)
    city = models.CharField(verbose_name=_('City'), max_length=100, null=True, blank=True, )
    slug_ar = models.SlugField(verbose_name=_('Slug Ar'), max_length=250, null=True, blank=True)
    slug = models.SlugField(verbose_name=_('Slug En'), max_length=250, null=True, blank=True)
    body_ar = models.TextField(verbose_name=_('Body Ar'), null=True, blank=True)
    body_en = models.TextField(verbose_name=_('Body En'), null=True, blank=True)
    feature_image = models.ImageField(verbose_name=_('Image'), null=True,
                                      blank=True,
                                      upload_to='pictures/',
                                      validators=[validate_file_extension])
    price = models.PositiveIntegerField(verbose_name=_('Price'), default=0, null=True, blank=True)
    allow_offer = models.PositiveIntegerField(verbose_name=_('Offer'), default=0, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True,
                                 related_name='category_products')
    status = models.BooleanField(verbose_name=_('Status'), default=True)  # publish - draft or hide - rejected by admin
    rejected_reason = models.TextField(verbose_name=_('Reason'), null=True, blank=True)
    view = models.PositiveIntegerField(verbose_name=_('Viewed'), default=1 ,null=True, blank=True)
    ip_address = models.GenericIPAddressField(
        default='0.0.0.0', verbose_name=_("ip address"), null=True, blank=True)
    added_by = models.CharField(verbose_name=_('Added By'), max_length=50, null=True, blank=True)
    added_on = models.DateTimeField(verbose_name=_('Added Date'), default=timezone.now, null=True, blank=True)
    updated_by = models.CharField(verbose_name=_('Updated By'), max_length=50, null=True, blank=True)
    updated_on = models.DateTimeField(verbose_name=_('Last Updated Date'), auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
        ordering = ['-updated_on']

    @property
    def title(self):
        lang = translation.get_language()
        if lang == "ar":
            return self.title_ar
        else:
            return self.title_en

    @property
    def body(self):
        lang = translation.get_language()
        if lang == "ar":
            return self.body_ar
        else:
            return self.body_en

    def __str__(self):
        return self.title

    # @property
    # def slug(self):
    #     lang = translation.get_language()
    #     if lang == "ar":
    #         return self.slug_ar
    #     else:
    #         return self.slug_en

    def save(self, *args, **kwargs):
        # if self.slug_ar in (None, '', u''):
        self.slug_ar = slugify(self.title_ar, allow_unicode=True)
        self.slug = slugify(self.title_en)
        # if self.slug_en in (None, '', u''):
        # self.slug_en = slugify(self.title_en)
        super(Product, self).save(*args, **kwargs)

    # @staticmethod
    # def get_visitors(self):
    #     return self.view + 1

    def get_absolute_url(self, **kwargs):
        return reverse('post:detail', kwargs={'product_id':self.pk,
                                              'country_slug':self.country.slug,
                                              'category_slug':self.category.slug,
                                              'slug': self.slug })
    # Todo: return slug_en and slug_ar based on lang

    # def get_absolute_url(self, **kwargs):
    #     lang = translation.get_language()
    #     if lang == "ar":
    #         return reverse('post:detail', kwargs={'slug': self.slug_ar})
    #     if lang == "en":
    #         return reverse('post:detail', kwargs={'slug': self.slug_en})

    @staticmethod
    def get_category_products(category):
        # return Product.objects.filter(category=category).order_by('-created_date').exclude(show=False)
        return Product.objects.filter(category=category)

    @staticmethod
    def get_country_products(country):
        # return Product.objects.filter(category=category).order_by('-created_date').exclude(show=False)
        return Product.objects.filter(country=country)

    @staticmethod
    def get_country_category_products(country, category):
        return Product.objects.filter(country=country, category=category)

    # @staticmethod
    # def increase_visit_count(self, commit=False):
    #     self.view += 1
    #     if commit:
    #         self.save()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                verbose_name=_('Product ID'),
                                related_name='images', blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', verbose_name=_('Image'))

    def __str__(self):
        return self.product.title_en


class Country(models.Model):
    name_ar = models.CharField(verbose_name=_('Country Ar'), max_length=100, null=True, blank=True, )
    name_en = models.CharField(verbose_name=_('Country En'), max_length=100, null=True, blank=True, )
    slug = models.SlugField(verbose_name=_('Slug'), max_length=100, null=True, blank=True, )
    display = models.BooleanField(verbose_name=_('Display'), default=True)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    @property
    def country(self):
        lang = translation.get_language()
        if lang == "ar":
            return self.name_ar
        else:
            return self.name_en

    def __str__(self):
        return self.country if self.country else str(self.pk)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)
        super(Country, self).save(*args, **kwargs)

    @staticmethod
    def get_country_by_slug(slug):
        try:
            return Country.objects.get(slug=slug)
        except:
            pass


class Category(models.Model):
    name_ar = models.CharField(verbose_name=_('Category Name Ar'), max_length=100, null=True, blank=True)
    name_en = models.CharField(verbose_name=_('Category Name En'), max_length=100, null=True, blank=True)
    image = models.ImageField(verbose_name=_('Image'), null=True,
                              blank=True,
                              upload_to='categories/',
                              validators=[validate_file_extension])
    slug = models.SlugField(verbose_name=_('Slug En'), max_length=250, null=True, blank=True)
    show = models.BooleanField(verbose_name=_('show'), default=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name_en

    @property
    def category_name(self):
        lang = translation.get_language()
        if lang == "ar":
            return self.name_ar
        else:
            return self.name_en

    def save(self, *args, **kwargs):
        # if self.slug_ar in (None, '', u''):
        self.slug = slugify(self.name_en)
        super(Category, self).save(*args, **kwargs)

    @property
    def product_count(self):
        # Todo: filter by country and city
        return self.category_products.count()

    @staticmethod
    def get_categories():
        return Category.objects.filter(show=True)

    @staticmethod
    def get_categories_by_country(country):
        return Category.objects.filter(country=country)
    # @staticmethod
    # def get_category(category):
    #     try:
    #         return Category.objects.get(name_en__iexact=category)
    #     except:
    #         return Category.objects.none()

    @staticmethod
    def get_category_by_slug(slug):
        try:
            return Category.objects.get(slug=slug)
        except:
            pass


class Message(models.Model):
    pass
