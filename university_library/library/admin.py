from django.contrib import admin
from .models import (
    Student,
    StudentGroup,
    LibraryCard,
    Literature,
    BookBorrowing,
    Librarian,
    LibraryDepartment,
    BookTag
)

admin.site.register(Student)
admin.site.register(StudentGroup)
admin.site.register(LibraryCard)
admin.site.register(Literature)
admin.site.register(BookBorrowing)
admin.site.register(Librarian)
admin.site.register(LibraryDepartment)
admin.site.register(BookTag)