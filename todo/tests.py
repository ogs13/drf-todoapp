from django.test import TestCase
from .models import Todo

class TodoTest(TestCase):
    """ Test module for Puppy model """
    def setUp(self):
        Todo.objects.create(
            title='first todo', 
            description='first todo description'
        )
        Todo.objects.create(
            title='second todo', 
            description='second todo description',
            done=True
        )
    
    def test_todo(self):
        first_todo = Todo.objects.get(title='first todo')
        self.assertEqual(first_todo.description, 'first todo description')
        self.assertEqual(first_todo.done, False)
        
        second_todo = Todo.objects.get(title='second todo')
        self.assertEqual(second_todo.description, "second todo description")
        self.assertEqual(second_todo.done,True)