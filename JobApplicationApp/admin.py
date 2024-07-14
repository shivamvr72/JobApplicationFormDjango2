from django.contrib import admin
from .models import User,BasicDetails, LanguagesKnown, EducationDetails


# Register your models here.
admin.site.register(User)
admin.site.register(BasicDetails)
# admin.site.register(Languages)
admin.site.register(LanguagesKnown)
# admin.site.register(LangaugeAbility)
admin.site.register(EducationDetails)
