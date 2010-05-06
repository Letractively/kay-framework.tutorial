# -*- coding: utf-8 -*-
"""
myapp.views
"""

from werkzeug import redirect

from kay.utils import (
  render_to_response, url_for
)
from kay.auth.decorators import login_required

from myapp.models import Comment
from myapp.forms import CommentForm


ITEMS_PER_PAGE = 20

# Create your views here.

@login_required
def index(request):
  form = CommentForm()
  if request.method == "POST" and form.validate(request.form):
    form.save()
    return redirect(url_for('myapp/index'))
  query = Comment.all().order('-created')
  comments = query.fetch(ITEMS_PER_PAGE)
  return render_to_response('myapp/index.html',
                            {'form': form.as_widget(),
                             'comments': comments})
