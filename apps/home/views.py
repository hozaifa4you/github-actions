from django.shortcuts import render

from .models import Home

FEATURES = [
    {
        "title": "Template rendering",
        "body": "home.html extends base.html and is discovered through APP_DIRS template loading.",
    },
    {
        "title": "Static files",
        "body": "Tailwind compiles static/css/input.css into static/dist/output.css, loaded with {% static %}.",
    },
    {
        "title": "Model data",
        "body": "The view queries the Home model and the template renders it with an empty state fallback.",
    },
]


def home(request):
    context = {
        "features": FEATURES,
        "entries": Home.objects.order_by("-created_at"),
    }
    return render(request, "home.html", context)
