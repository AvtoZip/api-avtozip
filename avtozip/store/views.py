"""Store application views."""

from django.shortcuts import render

from .api.resources import ProductResource
from .forms import ProductFormSet


def index_view(request):
    """INDEX view of store application."""
    if request.method == 'POST':
        formset = ProductFormSet(request.POST)
        if formset.is_valid():
            formset.save()

    if request.method != 'POST' or formset.is_valid():
        res = ProductResource()
        request_bundle = res.build_bundle(request=request)
        formset = ProductFormSet(queryset=res.obj_get_list(request_bundle))

    context = {
        'formset': formset,
    }

    return render(request, 'store/index.html', context)
