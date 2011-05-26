# coding: utf-8
from django import forms
from django.contrib.auth.models import User

from team.models import Team, TeamMember
from constants import MEMBERTYPE_CHOICES, ADMIN

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
    

class TeamMemberForm(forms.Form):
  username = forms.CharField( label = "Identifiant" )
  team = forms.ModelChoiceField( label = "Equipe", queryset = Team.objects.all() )
  member_type = forms.ChoiceField( label = "Type d'utilisateur", choices = MEMBERTYPE_CHOICES, required = False )
  first_name = forms.CharField( label = "Prénom", required = False )
  last_name = forms.CharField( label = "Nom", required = False )
  email = forms.EmailField( label = "Email" )
  
  def __init__( self, instance = None, is_admin = False, *args, **kwargs ):
    super( TeamMemberForm, self ).__init__( *args, **kwargs )
    
    if instance:
      self.fields['username'].initial = instance.user.username
      self.fields['team'].initial = instance.team.id
      self.fields['first_name'].initial = instance.user.first_name
      self.fields['last_name'].initial = instance.user.last_name
      self.fields['email'].initial = instance.user.email
      self.fields['member_type'].initial = instance.member_type
      
      if not is_admin:
        self.fields['team'].widget.attrs.update({'disabled':'disabled'})
        self.fields['member_type'].widget.attrs.update({'disabled':'disabled'})
        self.fields['username'].widget.attrs.update({'disabled':'disabled'})
    
  
