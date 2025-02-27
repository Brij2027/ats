from django.db.models import Q, Case, Sum, When, Value, IntegerField
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from .models import Candidate
from .serializers import CandidateSerializer

# Create your views here.
class CreateCandidateView(CreateAPIView):
    serializer_class = CandidateSerializer

class UpdateDestroyCandidateView(RetrieveUpdateDestroyAPIView):
    http_method_names = ['put', 'patch', 'delete']
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class SearchView(ListAPIView):
    serializer_class = CandidateSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        
        if not query:
            Candidate.objects.none()
        
        # splitting name based on spaces to get separate words
        vector_tokens = query.split(" ")

        search_filter = Q()
        match_annotation = 0
        weightage = len(vector_tokens)
        for token in vector_tokens:
            search_filter |= Q(name__icontains = token)

            # prepare ranking annotation
            match_annotation += Sum(Case(
                            When(name__icontains=token, then=Value(weightage)),
                            default=Value(0),
                            output_field=IntegerField()
                        ))

            weightage -= 1

        queryset = Candidate.objects.filter(search_filter)
            
        queryset = queryset.annotate(match_count=match_annotation)

        return queryset.order_by('-match_count')

