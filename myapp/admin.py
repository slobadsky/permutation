from django.contrib import admin
from myapp.models import Permutation

# Register your models here.

@admin.register(Permutation)
class PermutationAdmin(admin.ModelAdmin):
    list_display = ("permut_demandant","permut_start_datetime", "permut_end_time", "permut_acceptant","permut_acceptant_start_datetime","permut_acceptant_end_time")
    
