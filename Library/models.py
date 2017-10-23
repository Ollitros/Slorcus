from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=48)
    sur_name = models.CharField(max_length=48)

    def __str__(self):
        return "%s %s" % (self.name, self.sur_name)

    class Meta:
        verbose_name_plural = "Authors"
        verbose_name = "Author"


class Genre(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name_plural = "Genres"
        verbose_name = "Genre"


class Book(models.Model):
    name = models.CharField(max_length=48)
    author = models.ForeignKey(Author, blank=True, null=True, default=None)
    genre = models.ForeignKey(Genre, blank=True, null=True, default=None)
    price = models.CharField(max_length=32)
    description = models.TextField(max_length=4096)

    def __str__(self):
        return "%s %s" % (self.name, self.author)

    class Meta:
        verbose_name_plural = "Books"
        verbose_name = "Book"


class BookPicture(models.Model):
    product = models.ForeignKey(Book, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='book_images/')

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name_plural = "Images"
        verbose_name = "Image"
