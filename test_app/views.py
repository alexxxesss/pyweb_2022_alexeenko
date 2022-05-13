from datetime import datetime
from random import random

from django.views import View
from django.http import HttpRequest, HttpResponse


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)


class RandomNumberView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        random_number = random()

        return HttpResponse(random_number)
