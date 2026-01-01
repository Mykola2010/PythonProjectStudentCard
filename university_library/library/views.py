from django.shortcuts import render
from .models import Student, Literature, BookBorrowing

def students_view(request):
    return render(request, 'library/students.html', {
        'students': Student.objects.all()
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


