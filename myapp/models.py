from django.db import models
from django.contrib.auth.models import User
from crum import get_current_user
import random

# Create your models here.

def random_unique_number():
    return ''.join(random.choice('0123456789') for x in range(19))


def random_unique_string():
    return ''.join(random.choice('abcdefghijkmnpqrstuvwxyzxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789') for x in range(128))



class Permutation(models.Model):
    permut_start_datetime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True,verbose_name=('permut_start_datetime'))
    permut_end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True,verbose_name=('permut_end_time'))
    permut_demandant = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='permut_demandant_related', verbose_name=('permut_demandant'))
    permut_acceptant_start_datetime = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True,verbose_name=('permut_accept_start_datetime'))
    permut_acceptant_end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True,verbose_name=('permut_accept_end_time'))
    permut_acceptant = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='permut_acceptant_related', verbose_name=('permutant'))
    permut_created_at = models.DateTimeField(auto_now_add=True, verbose_name=('permut_created_at'))
    permut_updated_at = models.DateTimeField(auto_now=True, verbose_name=('permut_updated_at'))    
    permut_unique_ref = models.CharField(max_length=255,unique=True,default=random_unique_string,verbose_name=('permut_unique_ref'))
    permut_num_ref = models.CharField(null=True,max_length=255,unique=True,default =random_unique_number,verbose_name=('permut_number_ref'))
    permut_motif = models.CharField(max_length=255,blank=True, null=True, verbose_name=('permut_motif'))
    permut_accepted=models.BooleanField(default=False, verbose_name=('permut_accepted'))
    
    
    class Meta:
        db_table = "permutation"
        verbose_name = "permutation"
        verbose_name_plural = "permutations"
        
    """def __str__(self):
        return '%s %s' % (self.myuser_first_name,self.myuser_first_name)"""
    
