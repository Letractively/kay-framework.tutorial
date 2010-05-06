# -*- coding: utf-8 -*-
# Kay application: myapp

from google.appengine.ext import db

from kay.utils.db_hook import register_pre_delete_hook

from myapp.models import (
  Comment, Category
)

def cascade_delete(key):
  entities = Comment.all(keys_only=True).filter('category =', key).fetch(2000)
  db.delete(entities)

register_pre_delete_hook(cascade_delete, Category)
