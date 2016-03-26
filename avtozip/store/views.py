"""Store application views."""

from django.shortcuts import render


# TODO should be deleted as first real view is created
def fake_view(request):
    """Fake view like a placeholder."""
    return render(request, template_name='fake_name.html')
# TODO end
