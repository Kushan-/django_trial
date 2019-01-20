from django.apps import AppConfig


class FetchdataConfig(AppConfig):
    name = 'fetchData'

    def ready(self):
        super(ContentAppConfig, self).ready()
