from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from actionstep.views import end_oauth_view, start_oauth_view
from caller.views import answer_view, collect_view, message_view
from core import views as core_views
from webhooks.views import jotform_form_view, webflow_form_view

router = routers.SimpleRouter()
router.register("upload", core_views.UploadViewSet, basename="upload")
router.register("submission", core_views.SubmissionViewSet, basename="submission")

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("actionstep/start/", start_oauth_view, name="actionstep-start"),
    path("actionstep/end/", end_oauth_view, name="actionstep-end"),
    path("caller/answer/", answer_view, name="caller-answer"),
    path("caller/collect/", collect_view, name="caller-collect"),
    path("caller/message/", message_view, name="caller-message"),
    path("api/webhooks/webflow-form/", webflow_form_view, name="webflow-form"),
    path("api/webhooks/jotform-form/", jotform_form_view, name="jotform-form"),
    path("api/", include(router.urls)),
    # Case app owns all the other URLs.
    path("", include("case.urls")),
]
