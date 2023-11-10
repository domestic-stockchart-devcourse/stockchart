from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        from .tasks import crawl_news, crawl_chart
        crawl_news()
        crawl_chart()
