from django.contrib import admin
from .models import task_data, prompt_data, new_text_data, prompt_and_response_data

admin.site.register(task_data)
admin.site.register(prompt_data)
admin.site.register(new_text_data)
admin.site.register(prompt_and_response_data)
