import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from candidate.models import Candidate

from utils import UrlUtils

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_candidate():
    return Candidate.objects.create(
        name="Ajay Kumar Yadav", 
        age=25, 
        gender="M", 
        email="ajay@example.com", 
        phone_number="+911234567890"
    )

# Test for creating a candidate
@pytest.mark.django_db
def test_create_candidate(api_client):
    url = reverse(UrlUtils.CANDIDATE_CREATE_VIEW)
    data = {
        "name": "John Doe",
        "age": 30,
        "gender": "M",
        "email": "john@example.com",
        "phone_number": "+919876543210"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == data['name']
    assert response.data['email'] == data['email']

# Test for updating a candidate
@pytest.mark.django_db
def test_update_candidate(api_client, create_candidate):
    url = reverse(UrlUtils.CANDIDATE_UPDATE_DELETE_VIEW, args=[create_candidate.id])  
    data = {
        "name": "John Updated",
        "age": 31,
        "gender": "M",
        "email": "johnupdated@example.com",
        "phone_number": "+919876543210"
    }
    response = api_client.put(url, data, format='json')
    print(response.__dict__)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == data['name']
    assert response.data['email'] == data['email']

# Test for deleting a candidate
@pytest.mark.django_db
def test_delete_candidate(api_client, create_candidate):
    url = reverse(UrlUtils.CANDIDATE_UPDATE_DELETE_VIEW, args=[create_candidate.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Candidate.objects.filter(id=create_candidate.id).count() == 0


# Test for searching candidates with multiple similar name matches (like 'Ajay Kumar' etc.)
@pytest.mark.django_db
def test_search_candidates_multiple_matches(api_client):
    Candidate.objects.create(name="Ajay Kumar Yadav", age=28, gender="M", email="ajaykumar@example.com", phone_number="1234567890")
    Candidate.objects.create(name="Ajay Kumar", age=30, gender="M", email="ajay@example.com", phone_number="9876543210")
    Candidate.objects.create(name="Ajay Yadav", age=27, gender="M", email="ajayyadav@example.com", phone_number="1122334455")
    Candidate.objects.create(name="Kumar Yadav", age=29, gender="M", email="kumaryadav@example.com", phone_number="5566778899")
    Candidate.objects.create(name="Ajay Singh", age=26, gender="M", email="ajaysingh@example.com", phone_number="6677889900")
    Candidate.objects.create(name="Ramesh Yadav", age=35, gender="M", email="rameshyadav@example.com", phone_number="9988776655")

    url = reverse(UrlUtils.SEARCH_CANDIDATE_BY_NAME)  
    query_params = {'q': 'Ajay Kumar Yadav'}
    response = api_client.get(url, query_params, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0

    names = [candidate['name'] for candidate in response.data]
    assert "Ajay Kumar Yadav" in names
    assert "Ajay Kumar" in names
    assert "Ajay Yadav" in names
    assert "Kumar Yadav" in names
    assert "Ajay Singh" in names  
    assert "Ramesh Yadav" in names

    assert names.index('Ajay Kumar Yadav') < names.index('Ajay Kumar')
    assert names.index('Ajay Kumar') < names.index('Ajay Yadav')
    assert names.index('Ajay Yadav') < names.index('Kumar Yadav')
    assert names.index('Ajay Singh') < names.index('Ramesh Yadav')



