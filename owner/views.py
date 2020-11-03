from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from home_app.models import ContactModel
from django.shortcuts import render, redirect
from .models import InfomationModel, SkillModel, PictureModel
from .form import InformationForm, SkillForm, PictureForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages




# Home preview
@login_required
def home(request):
    task = InfomationModel.objects.all()
    skill = SkillModel.objects.all()
    photo = PictureModel.objects.all()
    return render(request, 'home.html', {'data':task, 'skill': skill, 'photo': photo})

# Edit Name, working and skill description
@login_required
def edit(request, id):
    if request.method == 'POST':
        task = InfomationModel.objects.get(id=id)
        form = InformationForm(request.POST or None , instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Edit Successfully')
            
        else:
            messages.error(request, 'Somethings went Wrong')
        return redirect('home')
    else:
        task = InfomationModel.objects.get(id=id)
        return render(request, 'edit.html', {'task':task})

# Add Skill
@login_required
def add(request):
    if request.method == 'POST':
        task = SkillForm(request.POST or None)
        if task.is_valid():
            task.save()
            messages.success(request, 'Skill added successfully')
        else:
            messages.error(request, 'Somethings went Wrong')
        return redirect('home')
    
    else:
        return render(request, 'add_skill.html')

# Edit Skill
@login_required
def edit_skill(request, id):
    if request.method == 'POST':
        task = SkillModel.objects.get(id =id)
        form = SkillForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill Edit Successfully')
        else:
            messages.error(request, 'Somethings went Wrong')
        return redirect('home')
    else:
        task = SkillModel.objects.get(id=id)
        return render(request, 'edit_skill.html', {'task':task})

# Edit Profile images
@login_required
def edit_img(request, id):
    if request.method == 'POST':
        task = PictureModel.objects.get(id=id)
        form = PictureForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Picture Changed Successfully')
        else:
            messages.error(request, 'Somethings went Wrong')

        return redirect('home')

    else:
        return render(request, 'edit_img.html')

# Edit About page Image
@login_required
def edit_about_img(request, id):
    if request.method == 'POST':
        task = PictureModel.objects.get(id =id)
        form = PictureForm(request.POST, request.FILES, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'About Picture Added Successfully')
        else:
            messages.error(request, 'Somethings went Wrong')
        return redirect('home')

    else:
        return render(request, 'edit_about_img.html')

# Delete SKill
@login_required
def delete_skill(request, id):
    task = SkillModel.objects.get(id = id)
    task.delete()
    messages.success(request, 'Skill Deleted SuccessFully')
    return redirect('home')

# Messag section
@login_required
def msg(request):
    task = ContactModel.objects.all()
    return render(request, 'message.html', {'msg': task})

# Delete Message Section
@login_required
def delete_msg(request, id):
    task = ContactModel.objects.get(id = id)
    task.delete()
    messages.success(request, 'Deleted Message SuccessFully')
    return redirect('msg')

# Send Email
def send_email(request):
    name = request.POST.get('name', '')
    from_email = request.POST.get('email', '')
    message = request.POST.get('des', '')
    if subject and message and from_email:
        try:
            send_mail(name, message, from_email, ['2809sourabh@gmaile.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')