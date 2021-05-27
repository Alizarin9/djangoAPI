from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task_data', views.task_data_view),
router.register('prompt_data', views.prompt_data_view),
router.register('new_text_data', views.new_text_data_view),
router.register('prompt_and_response', views.prompt_and_response_data_view),

urlpatterns = [
    path('', include(router.urls)),
]