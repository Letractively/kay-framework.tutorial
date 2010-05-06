# -*- coding: utf-8 -*-

from kay.utils import forms
from kay.utils.forms.modelform import ModelForm

from myapp.models import Comment

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    exclude = ('user', 'created')
