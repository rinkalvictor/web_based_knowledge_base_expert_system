from django.contrib.auth.models import Group
from django import template

register = template.Library()

@register.filter(name='has_group') 
def has_group(user, experts): 
	return user.groups.filter(name='experts').exists()