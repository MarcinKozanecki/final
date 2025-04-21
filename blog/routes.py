from flask import render_template, request, Blueprint, redirect, url_for
from blog import db
from blog.models import Entry
from blog.forms import EntryForm

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    all_posts = Entry.query.filter_by(is_published=True).order_by(Entry.date_posted.desc())
    return render_template("homepage.html", all_posts=all_posts)

@bp.route("/new-post/", methods=["GET", "POST"])
def create_entry():
    form = EntryForm()
    if form.validate_on_submit():
        entry = Entry(
            title=form.title.data,
            body=form.body.data,
            is_published=form.is_published.data
        )
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template("entry_form.html", form=form)


@bp.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
def edit_entry(entry_id):
   entry = Entry.query.filter_by(id=entry_id).first_or_404()
   form = EntryForm(obj=entry)
   errors = None
   if request.method == 'POST':
       if form.validate_on_submit():
           form.populate_obj(entry)
           db.session.commit()
       else:
           errors = form.errors
   return render_template("entry_form.html", form=form, errors=errors)