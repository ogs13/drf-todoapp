import json
from django.test import TestCase,Client
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer

client = Client()

TODO_API_URL = '/api/todos/'

class GetAllTodoTest(TestCase):
    """ Test module for GET all puppies API """
    def setUp(self):
        self.third_todo= Todo.objects.create(
            title='third todo', 
            description='third todo description'
        )
        Todo.objects.create(
            title='fourth todo', 
            description='fourth todo description',
            done=True
        )

        self.valid_payload = {            
            'title':'fifth todo', 
            'description':'fifth todo description',            
        }
        self.invalid_payload = {
            'title': '',
            'description': 4,
        }
    
    def test_get_all_todos(self):
        
        # get API response
        response = client.get(TODO_API_URL)
        # get data from db
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_invalid_single_todo(self):
        response = client.get(f'{TODO_API_URL}30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_create_valid_todo(self):
        response = client.post(
            TODO_API_URL,
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_todo(self):
        response = client.post(
            TODO_API_URL,
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    
    def test_valid_update_todo(self):
        response = client.put(
            f'{TODO_API_URL}{self.third_todo.pk}/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_invalid_update_todo(self):
        response = client.patch(
            f'{TODO_API_URL}{self.third_todo.pk}/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

    def test_valid_delete_todo(self):
        response = client.delete(f'{TODO_API_URL}{self.third_todo.pk}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    def test_invalid_delete_todo(self):
        response = client.delete(f'{TODO_API_URL}30/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
