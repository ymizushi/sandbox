# -*- coding: utf-8 -*-

from flask import Blueprint

mod = Blueprint('admin', __name__, url_prefix='/admin')

@mod.route('/')
def index():
    return "admin/", 200
#
@mod.route('/login', methods=['GET', 'POST'])
def login():
    return "admin/login", 200



