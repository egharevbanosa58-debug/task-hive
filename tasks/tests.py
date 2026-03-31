from django.test import TestCase
from django.urls import reverse # Looks up my URL by its (name) 
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APITestCase # Special Version oof Django's Testing tool made specifically for APIs

from .models import Task

# Create your tests here.

class TaskTests(APITestCase):

    def setUp(self):
        # This function runs before every single test, so we can use it to set up any data we need for our tests
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # This tells the test runner: Pretend like this user is logged in for all requests
        self.client.force_authenticate(user=self.user)

    def test_can_create_task(self): # Every test function should start with the word 'test_'
        url = reverse('tasks-list')

        data = {'title': 'Test Task', 'description': 'This is my first test task', 'status': 'TODO'}

        response = self.client.post(url, data, format='json')

        # The Checks
        # Did the server return "201 created"?
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Is there now 1 task in our temporary database?
        self.assertEqual(Task.objects.count(), 1)

        # Does that task have the right title?
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_can_list_tasks(self):
        # Creating a task in the temporary database first
        Task.objects.create(title="Existing Task", description="This task already Exists bahaha and i am testing GET by the way",user=self.user)

        # Hit the list URL
        url = reverse('tasks-list')
        response = self.client.get(url)

        # The Checks
        # Did the server return "200 OK"?
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # response.data is the JSON list Reast would see :)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Existing Task')

    def test_can_delete_task(self):
        # Creating a task to delete
        task = Task.objects.create(title="Task to delete", description="Unfortunately you have to go :()", user=self.user)

        # Get the specific url for that task (using its ID)
        url = reverse('tasks-detail', kwargs={'pk': task.id})

        # Hit the delete Endpoint
        response = self.client.delete(url)

        # The Checks
        # Did the server return the "204 No Content"?
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Is the task really deleted?
        self.assertEqual(Task.objects.count(), 0)