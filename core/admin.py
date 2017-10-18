from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.forms import UserChangeForm, UserCreationForm
from core.models import User, MedicalRecord, Prescription, Medicine, Approval


class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'name', 'is_staff', 'user_type',)
    list_filter = ('is_staff', 'user_type')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info/Business info',
         {'fields': ('name', 'phone', 'user_type')}),
        ('Permissions', {'fields': (
            'groups', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'password1', 'password2')}),
        ('Personal info/Business info',
         {'fields': ('name', 'phone', 'user_type')}),
        ('Permissions', {'fields': (
            'groups', 'is_staff', 'is_active')}),
    )
    search_fields = ('email', 'name',)
    ordering = ('name', 'user_type')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, CustomUserAdmin)


@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    pass


class MedicineInlineAdmin(admin.StackedInline):
    model = Medicine
    extra = 1


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    inlines = [MedicineInlineAdmin]


@admin.register(Approval)
class ApprovalAdmin(admin.ModelAdmin):
    pass
