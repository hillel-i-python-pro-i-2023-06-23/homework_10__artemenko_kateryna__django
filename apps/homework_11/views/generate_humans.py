from django.shortcuts import render

from apps.homework_11.services.generate_humans import generate_humans


def generate_humans_view(
        request,
        amount: int = 10,
):
    humans = generate_humans(amount=amount)

    return render(
        request=request,
        template_name="homework_11/generate_humans.html",
        context=dict(
            humans=humans,
        ),
    )
