from django.http import HttpResponse
from django.views import View

from .models import SomeModel


class LoadedView(View):
    def get(self, request, *args, **kwargs):
        SomeModel().save()
        return HttpResponse('Hello, World!')
