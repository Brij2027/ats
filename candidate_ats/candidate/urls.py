from django.urls import path

from .views import CreateCandidateView, UpdateDestroyCandidateView
from utils import UrlUtils

urlpatterns = [
    path('candidates/api/v1/', CreateCandidateView.as_view(http_method_names=["post"]), name=UrlUtils.CANDIDATE_CREATE_VIEW),
    path('candidates/api/v1/<int:pk>/', UpdateDestroyCandidateView.as_view(http_method_names=["put","patch","delete"]), name=UrlUtils.CANDIDATE_UPDATE_DELETE_VIEW)
]