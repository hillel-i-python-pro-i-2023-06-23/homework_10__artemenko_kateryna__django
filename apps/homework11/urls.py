from django.urls import path, include

from apps.homework11 import views

app_name = "homework11"

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
