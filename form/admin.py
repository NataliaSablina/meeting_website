from django.contrib import admin

from form.models import Form, CommonData, Preferences, Type, DifferentInfo

admin.site.register(Form)
admin.site.register(CommonData)
admin.site.register(Preferences)
admin.site.register(Type)
admin.site.register(DifferentInfo)
