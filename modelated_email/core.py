from __future__ import unicode_literals

from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context, Engine
from django.template.loader import render_to_string

from . import settings as app_settings
from .models import EmailTemplate


class TemplateEmailMessage(EmailMessage):
    """
    Wrapper over standard class EmailMessage. The constructor takes `code` and `context` as
    mandatory arguments and returns an object of EmailMessage with `content_subtype` as `html`,
    also subject and body fields are filled in.
    """
    content_subtype = 'html'

    def __init__(self, code, context, language='en', **kwargs):
        ctx = Context(context)
        kw = kwargs.copy()

        email_template = EmailTemplate.objects.get(code=code)

        translated_field = '_' + language if app_settings.MODELATED_TRANSLATE else ''
        subject = getattr(email_template, 'subject{}'.format(translated_field))
        body = getattr(email_template, 'body{}'.format(translated_field))

        engine = Engine()
        subject = engine.from_string(subject)
        body = engine.from_string(body)
        kw['subject'] = subject.render(ctx)
        kw['body'] = body.render(ctx)
        super(TemplateEmailMessage, self).__init__(**kw)


def send_mail(code, to, context=None, language='en', attach_file=None):
    """
    :param code: string
    :param to: list
    :param context: dict
    :param language: str
    :param attach_file: str of file path
    :return: 0 or 1
    """
    msg = TemplateEmailMessage(code, context, language=language)
    msg.body = render_to_string('modelated_email/base.html',
                                {'content': msg.body,
                                 'language': language})

    msg.from_email = settings.DEFAULT_FROM_EMAIL
    msg.to = to
    if bool(attach_file):
        msg.attach_file(attach_file)
    return msg.send()
