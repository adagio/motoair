from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'polls.admin.MyAdminSite'


class PollsConfig(AppConfig):
    name = 'polls'
