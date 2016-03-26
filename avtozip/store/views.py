"""Store application views."""

from django.shortcuts import render


def index_view(request):
    """INDEX view of store application."""
    return render(request, 'store/index.html')
