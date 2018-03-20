from django.urls import path
from .apiviews import ChoiceList, CreateVote, PollViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = []
urlpatterns += router.urls
