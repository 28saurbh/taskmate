from django.shortcuts import render, HttpResponse, redirect
from owner.form import InformationForm
from owner.form import SkillModel , InfomationModel,  PictureModel
from .models import ContactModel
from .form import ContactForm
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == 'POST':
        task = ContactForm(request.POST or None)
        if task.is_valid():
            task.save()
            return HttpResponse("We are Contact as soon as Possible")
        else:
            return HttpResponse('Please try Again later, something went wrong')
        return redirect('welcome')
    else:
        task = InfomationModel.objects.all()
        skill = SkillModel.objects.all()
        photo = PictureModel.objects.all()
        return render(request, 'index.html', {'data': task, 'skill': skill, 'photo': photo})

# def name(request, id):
#     if request.method == 'POST':
#         form = InformationForm(request.POST or None)
#         if form.is_valid():
#             form.save()

#         return redirect('owner')

#     else:
#         task = infomation.objects.get(id=id)
#         return render(request, 'admin.html', {'data': task})
