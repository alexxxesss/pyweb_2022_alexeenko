from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse


class HelloView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        text = """<h1>Hello, World</h1>"""

        return HttpResponse(text)


class IndexView(View):
    def get(self, request):
        return render(request, 'common/index.html')
