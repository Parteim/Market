from django.contrib import admin

from .models import (
    BaseProductModel,
    MobilePhone,
    PC,
    TV,
)

admin.site.register(MobilePhone)
admin.site.register(PC)
admin.site.register(TV)