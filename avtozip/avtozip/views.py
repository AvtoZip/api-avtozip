"""AvtoZip Project views."""

from django.shortcuts import render


def dashboard_view(request):
    """General dashboard view of BackEnd."""
    return render(request, 'index.html')
