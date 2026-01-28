from django.contrib import admin
from django.urls import path
from journal_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index), # This makes the journal the home page
]