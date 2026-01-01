from django.db import models

class LibraryDepartment(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    department = models.ForeignKey(
        LibraryDepartment,
        on_delete=models.SET_NULL,
        null=True,
        related_name="librarians"
    )
    photo = models.ImageField(upload_to='librarians_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"



class BookTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


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

    tags = models.ManyToManyField(
        BookTag,
        blank=True,
        related_name="books"
    )

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

    librarian = models.OneToOneField(
        Librarian,
        on_delete=models.SET_NULL,
        null=True
    )

    borrow_date = models.DateField()

    def __str__(self):
        return f"{self.library_card} → {self.literature}"