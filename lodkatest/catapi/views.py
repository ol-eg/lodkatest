from rest_framework import generics

from lodkatest.catapi.serializers import CategorySerializer
from lodkatest.catapi.serializers import DetailsSerializer
from lodkatest.catapi.models import Category

class CategoriesView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent__isnull=True)

    def post_categories(self, serializer):
        serializer.save()

class DetailsView(generics.RetrieveAPIView):
    serializer_class = DetailsSerializer
    queryset = Category.objects.all()
