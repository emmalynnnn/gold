from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


def index(request):
    current_datetime = timezone.now()
    return render(request, 'gold/index.html', {'current_datetime': current_datetime})


def plan(request):
    return render(request, 'gold/plan.html', {})
