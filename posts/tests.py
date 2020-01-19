from django.test import TestCase
from .models import Tag, Post


class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(name='JavaScriptTC')

    def test_tag_has_name(self):
        tag = Tag.objects.get(name='JavaScriptTC')
