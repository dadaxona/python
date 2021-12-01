from django.test import TestCase
from  django.urls import reverse
from .models import Postlar
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self):
        Postlar.objects.create(title='Mavzu', author='malumot', body='body')

    def test_text_content(self):
        post = Postlar.objects.get(id=1)
        expected_objects_title = f'{post.title}'
        expected_objects_author = f'{post.author}'
        expected_objects_body = f'{post.body}'
        self.assertEqual(expected_objects_title, 'Mavzu')
        self.assertEqual(expected_objects_author, 'malumot')
        self.assertEqual(expected_objects_body, 'body')

class HomePageView(TestCase):
    def setUp(self):
        Postlar.objects.create(title='Mavzu 2', author='malumot2', body='body 2')

    def test_text_content_tyep(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)

    def test_text_content_tyepe(self):
        resp = self.client.get(reverse('nome'))
        self.assertEqual(resp.status_code, 200)

    def test_text_content_tyepem(self):
        resp = self.client.get(reverse('nome'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')