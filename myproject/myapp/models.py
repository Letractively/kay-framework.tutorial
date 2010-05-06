# -*- coding: utf-8 -*-
# myapp.models

from google.appengine.ext import db
from kay.auth.models import GoogleUser
import kay.db

# Create your models here.

class MyUser(GoogleUser):
  pass

class Category(db.Model):
  name = db.StringProperty(required=True)
  
  def __unicode__(self):
    return self.name

class Comment(db.Model):
  user = kay.db.OwnerProperty()
  category = db.ReferenceProperty(Category)
  body = db.StringProperty(required=True, verbose_name=u'Your Comment')
  created = db.DateTimeProperty(auto_now_add=True)

