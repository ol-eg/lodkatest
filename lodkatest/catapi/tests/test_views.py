import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from lodkatest.catapi.models import Category

class ViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def _test_post(self, endpoint, data):
        response = self.client.post(
                        reverse(endpoint),
                        data,
                        format='json'
        )
        self.assertEqual(
                    response.status_code,
                    status.HTTP_201_CREATED,
        )
        return response

    def test_can_create_category_no_children(self):
        catdata = {'name': 'Category 1', 'children': []}
        response = self._test_post('categories', catdata)
        self.assertEqual(json.dumps(catdata),
                         json.dumps(response.data))

    def test_can_create_category_with_child(self):
        catdata = {'name': 'C1', 'children':
                    [{'name': 'C11', 'children': []}]}
        response = self._test_post('categories', catdata)
        self.assertEqual(json.dumps(catdata),
                         json.dumps(response.data))

    def test_can_get_category(self):
        # if name is 11 -> parent is 1,
        # 11 node will have parent, children, and siblings
        categories = ['1','11','12','111','112']
        cat_objects = dict()
        for cat in categories:
            parent = cat_objects.get(cat[:-1],None)
            cat_obj = Category(name=cat, parent=parent)
            cat_obj.save()
            cat_objects[cat] = cat_obj

        cat = Category.objects.get(name='11')
        response = self.client.get(
            reverse('details',
            kwargs={'pk': cat.id}),
            format='json'
        )
        self.assertEqual(response.status_code,
                                status.HTTP_200_OK)
        expected = {'id': 2, 'name': '11',
                    'parents': [{'id': 1, 'name': '1'}],
                    'children': [{'id': 4, 'name': '111'},
                                 {'id': 5, 'name': '112'}],
                    'siblings': [{'id': 3, 'name': '12'}]}
        self.assertEqual(json.dumps(response.data),
                         json.dumps(expected))
