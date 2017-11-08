from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext as _

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form_template = 'admin/add_form.html'
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    # change_password_form = AdminPasswordChangeForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'active', 'staff', 'admin', 'last_login', 'date_joined', 'update')
    list_filter = ('admin', 'staff', 'active')
    fieldsets = (
        ('{} {} {}'.format(_('Email address'), _('and'), _('Password')), {'fields': ('email', 'password',)}),
        # (_('Personal info'), {'fields': ()}),
        (_('Permissions'), {
            # 'classes': ('collapse',),  # hide (show)
            'fields': (('admin', 'staff', 'active'),)
        }),
        # (_('Important dates'), {'fields': ('update',)}),
        (_('User permissions:'), {
            'fields':
                ('user_permissions',
                 # 'groups',
                 )
        }),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    empty_value_display = '-empty-'
    list_display_links = ('email',)
    list_editable = ('active',)  #edit

    class Meta:
        model = User


# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)









# from .models import UserProfile
#
# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', ]
#     # list_filter = ['name']
#     # prepopulated_fields = {"slug": ("name",)}
#
#     class Meta:
#         model = UserProfile
#
#
# admin.site.register(UserProfile, UserProfileAdmin)
