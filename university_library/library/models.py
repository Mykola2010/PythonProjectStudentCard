from django.db import models

class StudentGroup(models.Model):
    group_number = models.CharField(max_length=10, unique=True)
    slogan = models.CharField(max_length=255, blank=True)
    meeting_room = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.group_number


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_card_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    group = models.ForeignKey(
        StudentGroup,
        on_delete=models.SET_NULL,
        null=True,
        related_name="students"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class LibraryCard(models.Model):
    card_number = models.CharField(max_length=20, unique=True)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="library_card"
    )

    def __str__(self):
        return self.card_number


class Literature(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=150)
    publication_date = models.DateField()
    publication_year = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class BookBorrowing(models.Model):
    library_card = models.ForeignKey(
        LibraryCard,
        on_delete=models.CASCADE,
        related_name="borrowings"
    )


    literature = models.ForeignKey(
        Literature,
        on_delete=models.CASCADE,
        related_name="borrowings"
    )

    borrow_date = models.DateField()
    librarian_full_name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.library_card} → {self.literature}"
