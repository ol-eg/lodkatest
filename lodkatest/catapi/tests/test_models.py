from django.test import TestCase

from lodkatest.catapi.models import Category

class CategoryModelTest(TestCase):

    # if name is 11 -> parent is 1 etc
    categories = [
        '1','11','12','111','112','121',
        '122','1111','1112', '1113','1121',
        '1122','1123','1221','1222'
    ]

    def test_can_save_category(self):
        old_count = Category.objects.count()
        Category(name='C1').save()
        new_count = Category.objects.count()
        self.assertEqual(new_count-old_count, 1)

    def test_can_save_category_tree(self):
        old_count = Category.objects.count()
        count = 0
        cat_objects = dict()

        for i in CategoryModelTest.categories:
            parent = cat_objects.get(i[:-1],None)
            cat = Category(name=i, parent=parent)
            cat.save(0)
            count += 1
            cat_objects[i] = cat

        new_count = Category.objects.count()
        self.assertEqual(new_count-old_count, count)
