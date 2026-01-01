from django.shortcuts import render
from .models import Student, Literature, BookBorrowing, Librarian, LibraryDepartment

def home_view(request):
    return render(request, 'library/base.html')

def students_view(request):
    return render(request, 'library/students.html', {
        'students': Student.objects.select_related('group').all()
    })

def literature_view(request):
    return render(request, 'library/literature.html', {
        'literature': Literature.objects.all()
    })

def borrowings_view(request):
    return render(request, 'library/borrowings.html', {
        'borrowings': BookBorrowing.objects.select_related(
            'library_card__student',
            'literature'
        )
    })

def librarians_view(request):
    return render(request, 'library/librarians.html', {
        'librarians': Librarian.objects.select_related('department')
    })

def departments_view(request):
    return render(request, 'library/departments.html', {
        'departments': LibraryDepartment.objects.all()
    })

def tags_view(request):
    return render(request, 'library/tags.html', {
        'books': Literature.objects.prefetch_related('tags')
    })