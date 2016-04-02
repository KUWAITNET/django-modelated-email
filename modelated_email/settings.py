from django.conf import settings
from django.utils.module_loading import import_string


body_field = "ckeditor.fields.RichTextField" if \
    "ckeditor" in settings.INSTALLED_APPS else \
    "django.db.models.TextField"
translate = True if "modeltranslation" in settings.INSTALLED_APPS else False
admin_class = 'modeltranslation.admin.TabbedDjangoJqueryTranslationAdmin' \
    if translate else 'django.contrib.admin.ModelAdmin'

MODELATED_BODY_FIELD = getattr(settings, "MODELATED_BODY_FIELD", body_field)
MODELATED_TRANSLATE = getattr(settings, "MODELATED_TRANSLATE", translate)
MODELATED_ADMIN_CLASS = getattr(settings, "MODELATED_ADMIN_CLASS", admin_class)

BodyField = import_string(MODELATED_BODY_FIELD)
AdminClass = import_string(MODELATED_ADMIN_CLASS)
