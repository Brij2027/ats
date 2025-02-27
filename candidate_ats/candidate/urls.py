from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import CreateCandidateView, UpdateDestroyCandidateView, SearchView
from utils import UrlUtils

schema_view = get_schema_view(
   openapi.Info(
      title="Candidate API",
      default_version='v1',
      description="API for managing candidates and searching them"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('candidates/api/v1/', CreateCandidateView.as_view(), name=UrlUtils.CANDIDATE_CREATE_VIEW),
    path('candidates/api/v1/<int:pk>/', UpdateDestroyCandidateView.as_view(), name=UrlUtils.CANDIDATE_UPDATE_DELETE_VIEW),
    path('candidates/api/v1/search/', SearchView.as_view(), name=UrlUtils.SEARCH_CANDIDATE_BY_NAME),

    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='swagger-ui'),
]