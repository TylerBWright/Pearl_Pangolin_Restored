from django.shortcuts import render, redirect
from pp.forms import SubmissionForm

# Create your views here.


#class index(TemplateView):
 #   template_name = 'pearls/index.html'


#class about(TemplateView):
  #  template_name = 'pearls/about.html'


def index(request):
    return render(request, 'pearls/index.html')


def about(request):
    return render(request, 'pearls/about.html')


def play(request):
    return render(request, 'pearls/play.html')


def submit_animal(request):
    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():
            recipe = form.save(False)
            recipe.author = request.user
            recipe.save()
            return redirect("recipe_list")
    else:
        form = SubmissionForm()
    context = {
        "form": form,
    }
    return render(request, "pp/submit.html", context)
