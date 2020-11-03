from django import forms
from .models import InfomationModel, SkillModel, PictureModel

class InformationForm(forms.ModelForm):
    class Meta:
        model = InfomationModel
        fields = ['name', 'working','about', 'skilldes']


class SkillForm(forms.ModelForm):
    class Meta:
        model = SkillModel
        fields = ['SkName', 'percent']


class PictureForm(forms.ModelForm):
    class Meta:
        model = PictureModel
        fields = ['profile_picture', 'about_picture']