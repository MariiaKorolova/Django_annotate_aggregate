from datetime import timedelta

from django.shortcuts import redirect, render
from django.utils import timezone

from .forms import celery_ex_Form
from .tasks import send


def home(request):
    return render(request, "celery_ex/home.html")


def error(request):
    return render(request, "celery_ex/error.html")


def celery_ex(request):
    if request.method == "POST":
        celery_ex_form = celery_ex_Form(request.POST)
        if celery_ex_Form.is_valid():
            email = celery_ex_form.cleaned_data["email"]
            text_for_celery_ex = celery_ex_form.cleaned_data["text_for_celery_ex"]
            data_celery_ex = celery_ex_form.cleaned_data["data_celery_ex"]
            data_receive = timezone.now()
            data_between = data_receive + timedelta(days=2)
            if (data_celery_ex > data_receive) and (data_celery_ex <= data_between):
                send.s(email, text_for_celery_ex).apply_async(eta=data_celery_ex)
                return redirect('celery_ex:home')
            else:
                return redirect('celery_ex:error')
    else:
        celery_ex_form = Celery_ex_Form()
    return render(
        request,
        "celery_ex/celery_ex.html",
        {"celery_ex_form": celery_ex_form, }
    )