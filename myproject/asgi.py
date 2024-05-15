
from fastapi.staticfiles import StaticFiles
import os
from fastapi import FastAPI
from django.apps import apps
from django.conf import settings
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')



apps.populate(settings.INSTALLED_APPS)


application = get_asgi_application()

from app.endpoints import router

application = (FastAPI(openapi_url="/api/openAPI.json" , docs_url="/api/"))
application.include_router(router , prefix='/api')
application.mount("/",get_asgi_application())

