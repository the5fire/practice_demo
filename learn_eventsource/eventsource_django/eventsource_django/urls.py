from django.conf.urls import patterns

from django.views.generic import TemplateView

from .views import eventsource


urlpatterns = patterns(
    '',
    (r'^eventsource/$', eventsource),
    (r'^$', TemplateView.as_view(template_name="index.html")),
)
