# coding=utf-8
import jinja2
import webapp2

import settings


def render_template(name, parameters=None):
    template = settings.JINJA_ENVIRONMENT.get_template(name)
    rendered = template.render(parameters or {})
    return webapp2.Response(rendered)
