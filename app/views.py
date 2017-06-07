from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Professor
from app.forms import UserForm
from django.http.response import HttpResponse


class IndexView(TemplateView):
    def get(self, request):
        return render(request,
                      "app/index_main.html",
                      {'result': Professor.objects.all})

'''
class SignupView(TemplateView):
    def post(self, request):
        user_form = UserForm(data=request.POST)
        if user_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/app')
        return HttpResponseRedirect('/app/register')
    
    def get(self, request):
        form = UserForm()
        return render(request, 'signup.html', {'form': form})
'''


class SearchView(TemplateView):
    def post(self, request):
        return HttpResponse(request.body)
