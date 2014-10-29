from django.conf.urls import patterns

from django.views.generic import TemplateView

from .views import eventsource, ajax


urlpatterns = patterns(
    '',
    (r'^eventsource/$', eventsource),
    (r'^ajax/$', ajax),
    (r'^$', TemplateView.as_view(template_name="index.html")),
)
