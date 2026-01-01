from django.urls import path
from .views import students_view, literature_view, borrowings_view, librarians_view, departments_view, tags_view, home_view

urlpatterns = [
    path('students/', students_view, name='students'),
    path('literature/', literature_view, name='literature'),
    path('borrowings/', borrowings_view, name='borrowings'),
    path('librarians/', librarians_view, name='librarians'),
    path('departments/', departments_view, name='departments'),
    path('tags/', tags_view, name='tags'),
    path('', home_view, name='home'),

]
