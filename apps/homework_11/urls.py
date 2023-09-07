from django.urls import path, include

from apps.homework_11 import views

app_name = "homework_11"

urlpatterns = [
    path(
        "generate-humans/",
        include(
            [
                path("<int:amount>/", views.generate_humans_view, name="generate_humans_with_amount"),
                path("", views.generate_humans_view, name="generate_humans"),
            ]
        ),
    ),
]
