from flask import render_template, Blueprint
from . import db
from .models import Entry

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
      all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.date_posted.desc())

      return render_template("homepage.html", all_posts=all_posts)