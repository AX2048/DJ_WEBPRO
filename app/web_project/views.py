import os

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from .forms import NameForm

from .scripts.bg_text_create import create_text

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print(os.path.abspath(__file__))
            template = loader.get_template("index.html")
            print(form.data)
            from_field = form.cleaned_data['your_name']
            print(from_field)
            create_text(from_field, 'web_project/scripts/content/web_background_image.png', 'web_project/static/web_result_image.png', 'web_project/scripts/content/Archangelsk.ttf')
            return render(request, 'index.html', {'form': from_field, 'path': 'web_result_image.png'})#HttpResponse(template.render())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})