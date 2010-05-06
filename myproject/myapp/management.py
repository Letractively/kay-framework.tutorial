# -*- coding: utf-8 -*-

from google.appengine.ext import db

from kay.management.utils import (
  print_status, create_db_manage_script
)
from myapp.models import Category

categories = [
  u'Programming',
  u'Testing',
  u'Management',
]

def create_categories():
  entities = []
  for name in categories:
    entities.append(Category(name=name))
  db.put(entities)
  print_status("Categories are created succesfully.")

def delete_categories():
  db.delete(Category.all().fetch(100))
  print_status("Categories are deleted succesfully.")

action_create_categories = create_db_manage_script(
  main_func=create_categories, clean_func=delete_categories,
  description="Create 'Category' entities")
