import graphene
from .models import *
from duwin_backend.schemas import BaseType


class UserType(BaseType):
    """
    The User object.
    """
    class Meta:
        model = User
        fields = "__all__"


class AuthorType(BaseType):
    """
    This represents an Author object.
    """

    class Meta:
        model = Author
        fields = "__all__"


class BookType(BaseType):
    """
   This is the most fundamental model in the API, representing a Book object.
   A book can have many Authors, can belong to many Genres.
    """

    class Meta:
        model = Book
        fields = "__all__"


class GenreType(BaseType):
    """
    The Genre object.
    """

    class Meta:
        model = Genre
        fields = "__all__"


class LinkType(BaseType):
    """
    This is primarily made to store download sources (maybe from different domains,
    maybe different file types) of the Books.
    """

    class Meta:
        model = Link
        fields = "__all__"


class BookAuthorType(BaseType):
    """
    A bridge table for Books and Authors.
    """
    class Meta:
        model = BookAuthor
        fields = "__all__"


class BookGenreType(BaseType):
    """
    A bridge table for Books and Genres.
    """
    class Meta:
        model = BookGenre
        fields = "__all__"


class BookUserType(BaseType):
    """
    A bridge table for Books and Users. A User can add many Books to their
    Reading List or Favourites, and a Book can also belong to many Users'
    Reading Lists and Favourites. The "condition" parameter must be defined
    to specify whether to add to Reading List or Favourites.
    """

    class Meta:
        model = BookUser
        fields = "__all__"


class BookLinkType(BaseType):
    """
    A bridge table for Books and Links, for downloading from multiple sources.
    """
    class Meta:
        model = BookLink
        fields = "__all__"


# this is just like listing url endpoints.
fields = {
    "users": {"graphene":graphene.List, "type": UserType},
    "authors": {"graphene": graphene.List, "type": AuthorType},
    "books": {"graphene": graphene.List, "type": BookType},
    "genres": {"graphene": graphene.List, "type": GenreType},
    "links": {"graphene": graphene.List, "type": LinkType},
    "bookauthors": {"graphene": graphene.List, "type": BookAuthorType},
    "bookgenres": {"graphene": graphene.List, "type": BookGenreType},
    "bookusers": {"graphene": graphene.List, "type": BookUserType},
    "booklinks": {"graphene": graphene.List, "type": BookLinkType}
}


# creating the Query class and assigning attributes dynamically
Query = type("Query", (graphene.ObjectType,), {
    # re-written to a dict for better readability
    i[0]: i[1]["graphene"](i[1]["type"],
                           resolver=i[1]["type"].resolve,
                           **i[1]["type"].get_filter_fields())
    for i in fields.items()
})


