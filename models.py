from __future__ import unicode_literals
from django import forms
from django.db import models

#The website's contact form
class MessageModel(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(max_length=1000, null=True, blank=True)
    def __unicode__(self):
        return '%s) %s - %s: %s' % (self.pk, self.name, self.email, self.message[:20])

class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ('name', 'email','phone','message')
        widgets = {
                   'message': forms.Textarea(attrs={'class':'form-control', 'rows':'5', 'placeholder':'Your Message *'}),
                   'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
                   'email': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Email *'}),
                   'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Phone'},),
        }
