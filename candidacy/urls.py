from django.conf.urls import url

from .views import CandidacyView


urlpatterns = [
    url(r'^$', CandidacyView.as_view(), name='form'),
]
