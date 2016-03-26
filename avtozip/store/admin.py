"""Module to add Admin view functionality."""

from django.contrib import admin

from .models import Product


admin.site.register(Product)
