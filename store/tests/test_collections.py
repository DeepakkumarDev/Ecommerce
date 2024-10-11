import pytest
from rest_framework import status
from store.models import Collection,Product
from model_bakery import baker

@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection

@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        # Arrange, Act, Assert
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_collection):
        # Arrange
        authenticate()
        # Act
        response = create_collection({'title': 'a'})
        # Assert
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, authenticate, create_collection):
        # Arrange
        authenticate(is_staff=True)
        # Act
        response = create_collection({'title': ''})
        # Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, authenticate, create_collection):
        # Arrange
        authenticate(is_staff=True)
        # Act
        response = create_collection({'title': 'a'})
        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_if_collection_exits_returns_200(self,api_client):
        # Arrange
        # Collection.objects.create(title='a')

        collection = baker.make(Collection)
        # baker.make(Product,collection=collection,_quantity=10)
        response = api_client.get(f'/store/collections/{collection.id}/')

        # print(collection.__dict__)
        # assert False
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id':collection.id,
            'title':collection.title,
            'products_count':0

        }
        # assert response.data['id'] == collection.id 
        # assert response.data['title'] == collection.title 







































# from django.contrib.auth.models import User
# # from rest_framework.test import APIClient
# from rest_framework import status 
# from .conftest import api_client,authenticate
# import pytest


# @pytest.fixture
# def create_collection(api_client):
#     def do_create_collection(collection):
#         return api_client.post('/store/collections/',collection)
#     return do_create_collection








# @pytest.mark.django_db
# class TestCreateCollection:
#     # @pytest.mark.skip
#     def test_if_user_is_anonymous_returns_401(self,create_collection):
#         #AAA (Arrange,Act,Assert)
#         response = create_collection({'title':'a'})
        
#         # client = APIClient()
#         # response = api_client.post('/store/collections/')

#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     def test_if_user_is_not_admin__returns_403(self,authenticate,create_collection):
#         #AAA (Arrange,Act,Assert)
        
#         # client = APIClient()
#         # api_client.force_authenticate(user={})
#         authenticate()
#         response = create_collection({'title':'a'})
#         # response = api_client.post('/store/collections/',{'title':'a'})

#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_if_data_is_invalid__returns_400(self,authenticate,create_collection):
#         #AAA (Arrange,Act,Assert)
        
#         # client = APIClient()
#         # api_client.force_authenticate(user=User(is_staff=True))
#         authenticate(is_staff=True)
#         response = create_collection({'title':'a'})
#         # response = api_client.post('/store/collections/',{'title':''})

#         assert response.status_code == status.HTTP_400_BAD_REQUEST
#         assert response.data['title'] is not None 

#     def test_if_data_is_valid__returns_201(self,api_client,create_collection):
#         #AAA (Arrange,Act,Assert)
        
#         # client = APIClient()
#         api_client.force_authenticate(user=User(is_staff=True))
#         response = create_collection({'title':'a'})
#         # response = api_client.post('/store/collections/',{'title':'a'})

#         assert response.status_code == status.HTTP_201_CREATED
#         assert response.data['id'] > 0 

