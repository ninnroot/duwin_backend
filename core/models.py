from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .manager import CustomUserManager

from duwin_backend.models import BaseModel
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    ms_id = models.CharField(max_length=512,unique=True)
    role = models.CharField(
        max_length=8,
        # choices=(("SDM", "Super-admin"), ("ADM", "Admin"), ("USR", "User")),
        default="USR"
    )
    date_joined = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.email}-{self.id}"


class Author(BaseModel):

    name = models.CharField(max_length=512,
                            help_text="The author's name.")
    cover = models.ImageField(default="author_covers/default.jpg", upload_to="author_covers",
                              help_text="The author's cover image.")
    birth = models.DateField(help_text="The author's date of birth.")
    death = models.DateField(default=None, null=True,
                             help_text="The author's date of death. Null if the author is still alive.")
    description = models.TextField(help_text="The author's description. Saved in md format.")


class Book(BaseModel):

    title = models.CharField(max_length=512,
                             help_text="The title of the book.")
    published_date = models.DateField(null=True,
                                      help_text="The date of publication of the book. Null if unknown.")
    short_description = models.CharField(max_length=512,
                                         help_text="A short description.")
    long_description = models.TextField(help_text="A longer, more descriptive description. Saved in md format.")
    cover = models.ImageField(default="book_covers/default.jpg", upload_to="book_covers",
                              help_text="The cover image of the book.")
    length = models.IntegerField(help_text="The page count of the book.")


class Genre(BaseModel):

    name = models.CharField(max_length=512,
                            help_text="The name of the genre.")
    tagline = models.TextField(help_text="A brief description describing the genre.")
    cover = models.ImageField(default="genre_covers/default.jpg", upload_to="genre_covers",
                              help_text="The genre's cover image.")


class Link(BaseModel):

    name = models.CharField(max_length=512,
                            help_text="The name of the link.")
    url = models.URLField(max_length=512,
                          help_text="The url, yea, pretty self-explanatory.")


class BookAuthor(BaseModel):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookGenre(BaseModel):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class BookUser(BaseModel):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    condition = models.CharField(max_length=32, #choices=(("read", "read"), ("fav", "fav")),
                                 help_text="\"read\" to add to the user's Reading List, "
                                           "and \"fav\" for their Favourites")


class BookLink(BaseModel):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    link = models.ForeignKey(Link, on_delete=models.CASCADE)
