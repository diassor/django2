from django.views.generic.base import TemplateView
from django.shortcuts import render


# combiando funcion por clase
# def home(request):
#    return render(request, "core/home.html")
class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template_name,
                      {'title': "Mi super pagina de origami"})


# def sample(request):
#    return render(request, "core/sample.html")
class SamplePageView(TemplateView):
    template_name = "core/sample.html"
