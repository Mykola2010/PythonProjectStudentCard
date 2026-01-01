from django.urls import path
from .views import students_view, literature_view, borrowings_view

urlpatterns = [
    path('students/', students_view, name='students'),
    path('literature/', literature_view, name='literature'),
    path('borrowings/', borrowings_view, name='borrowings'),
]
