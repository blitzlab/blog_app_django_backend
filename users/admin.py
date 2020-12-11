from django.contrib import admin
from users.models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
# Register your models here.


class UserAdminConfig(UserAdmin):

    models = CustomUser

    search_fields = ("email", "first_name", "last_name", "user_name",)
    list_filter = ("email", "user_name", "first_name", "last_name", "is_active", "is_staff",)

    ordering = ("-registered_on",)

    list_display = ("first_name", "last_name", "email", "is_active", "is_staff", "registered_on")

    fieldsets = (
        (None, {"fields":("email", "user_name", "first_name", "last_name")}),
        ("Permissions", {"fields":("is_staff", "is_active",)}),
        ("Personal", {"fields":("about",)})
    )

    formfield_overrides = {
     # models.TextField: {"widget": Textarea(attrs={"rows":20, "cols": 60})},
    }

    add_fieldsets = (
        (None, {
            "classes":("wide",),
              "fields":("first_name", "last_name", "user_name", "email", "password1", "password2", "is_active")
        })
    )

admin.site.register(CustomUser, UserAdminConfig)
