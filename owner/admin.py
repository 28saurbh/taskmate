from django.contrib import admin
from .models import InfomationModel, SkillModel, PictureModel


# Register your models here.
admin.site.register(InfomationModel)
admin.site.register(SkillModel)
admin.site.register(PictureModel)