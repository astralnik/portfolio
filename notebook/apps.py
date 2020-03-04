from django.apps import AppConfig


class NotebookConfig(AppConfig):
    name = 'notebook'
    verbose_name = 'Ежедневник'     # Для отображения названия приложения в админке нужно еще в __init__.py добавить:
                                    # default_app_config = 'notebook.apps.NotebookConfig'
