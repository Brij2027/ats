from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Candidate
from .serializers import CandidateSerializer

# Create your views here.
class CreateCandidateView(CreateAPIView):
    serializer_class = CandidateSerializer

class UpdateDestroyCandidateView(RetrieveUpdateDestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer