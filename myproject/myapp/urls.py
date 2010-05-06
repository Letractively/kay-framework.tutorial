# -*- coding: utf-8 -*-
# myapp.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('myapp/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'myapp/index': 'myapp.views.index',
}
"""

from kay import generics
from kay.routing import (
  ViewGroup, Rule
)

class CategoryCRUDViewGroup(generics.CRUDViewGroup):
  model = 'myapp.models.Category'
  form = 'myapp.forms.CategoryForm'
  authorize = generics.admin_required

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='myapp.views.index'),
  ),
  CategoryCRUDViewGroup(),
]

