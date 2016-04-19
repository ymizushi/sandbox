from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

admin = Blueprint('admin', __name__, template_folder='admin')

@admin.route('/', defaults={'page': 'index'})
@admin.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
