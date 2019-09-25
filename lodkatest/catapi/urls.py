from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

from lodkatest.catapi.views import CategoriesView, DetailsView

urlpatterns = {
    path('categories/',
        CategoriesView.as_view(), name='categories'),
    path('categories/<int:pk>/',
        DetailsView.as_view(), name='details'),
}

urlpatterns = format_suffix_patterns(urlpatterns)
