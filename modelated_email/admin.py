from django.contrib import admin

from .settings import AdminClass, MODELATED_TRANSLATE
from .models import EmailTemplate


if MODELATED_TRANSLATE:
    from modeltranslation.translator import TranslationOptions, translator


    class EmailTemplateTranslationOptions(TranslationOptions):
        fields = ('subject', 'body',)

    translator.register(EmailTemplate, EmailTemplateTranslationOptions)


@admin.register(EmailTemplate)
class EmailTemplateAdmin(AdminClass):
    list_display = ("name", "subject")
    prepopulated_fields = {"code": ("name",)}
