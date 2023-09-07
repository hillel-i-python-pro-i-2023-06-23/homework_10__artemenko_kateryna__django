from django.shortcuts import render


def index(request):
    return render(
        request=request,
        template_name="base/home_page.html",
        context={
            "greetings_text": f"Hello, world!=)",
            "title": "Home page",
        },
    )
