from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import *


# @admin.register(ExtendedUser)
# class ExtendedUserAdmin(admin.ModelAdmin):
#     list_display = ('user', 'first_name', 'last_name', 'college', 'ambassador')
#     list_filter = ('ambassador', 'college')
#     search_fields = ['user__email', 'user__first_name', 'user__last_name', 'college', 'contact', 'city']

#     class Meta:
#         model = ExtendedUser
#         fields = '__all__'


@admin.register(ExtendedUser)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    # list_display = ('email', 'first_name', 'last_name', 'is_staff')
    # search_fields = ('email', 'first_name', 'last_name')
    # ordering = ('email',)
    list_display = ('email','first_name', 'last_name', 'college', 'ambassador')
    list_filter = ('ambassador', 'college')
    search_fields = ['email', 'first_name', 'last_name', 'college', 'contact', 'city']
    ordering = ('email',)

    class Meta:
        model = ExtendedUser
        fields = '__all__'


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'leader', 'event')
    list_filter = ('event',)
    search_fields = ['name', 'leader__email', ]


class SubmissionsAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'file_url')
    list_filter = ('event',)


class preregisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'college')
    list_filter = ('college',)

admin.site.register(Team, TeamAdmin)
admin.site.register(Submissions, SubmissionsAdmin)
admin.site.register(PreRegistration,preregisterAdmin)