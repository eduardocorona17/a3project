from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Widget

# Create your views here.

def index(request):
    widget = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widget})

class WidgetCreate(CreateView):
    model = Widget
    fields = "__all__"
    success_url = "/"