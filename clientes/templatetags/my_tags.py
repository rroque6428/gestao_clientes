import datetime

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return "%s - %s" % (context.request.user, datetime.datetime.now().strftime(format_string))
