from django.contrib import admin
from django.apps import apps

app_config = apps.get_app_config('inventory')
models = app_config.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
