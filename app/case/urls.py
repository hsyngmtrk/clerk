from django.urls import path

from . import views

urlpatterns = [
    # Paralegals
    path("paralegals/", views.paralegal.paralegal_list_view, name="paralegal-list"),
    path(
        "paralegals/<int:pk>/",
        views.paralegal.paralegal_detail_view,
        name="paralegal-detail",
    ),
    # Cases
    path("cases/", views.case.case_list_view, name="case-list"),
    path("cases/<uuid:pk>/", views.case.case_detail_view, name="case-detail"),
    path(
        "cases/<uuid:pk>/progress/",
        views.case.case_detail_progress_view,
        name="case-detail-progress",
    ),
    path(
        "cases/<uuid:pk>/progress/htmx/progress/",
        views.case.case_detail_progress_form_view,
        name="case-detail-progress-form",
    ),
    path(
        "cases/<uuid:pk>/progress/htmx/paralegal/",
        views.case.case_detail_paralegal_note_form_view,
        name="case-detail-paralegal-form",
    ),
    path(
        "cases/<uuid:pk>/progress/htmx/review/",
        views.case.case_detail_review_note_form_view,
        name="case-detail-review-form",
    ),
    path("", views.case.root_view, name="case-root"),
]
