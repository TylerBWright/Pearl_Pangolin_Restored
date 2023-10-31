from django.shortcuts import render, redirect

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
