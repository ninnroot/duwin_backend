import core.models as m

authors = [
    ("J. R. R. Tolkein", "1892-01-03", "1973-09-02", "# The father of fantasy literature.\n\nExtremely based man."),
    ("Dr. Seuss", "1904-03-02", "1991-09-24", "# Doctor Seuss\n\n You may know him from __The Lorax__.")
]

books = [
    ("The Hobbit", "1937-09-21", "yea, the hobbit", "# The Hobbit\n\n *J. R. R. Tolkien's* masterpiece.", 310),
    ("The Lord of the Rings", "1954-07-29", "Epic high-fantasy novel by Sir J. R. R. Tolkein", "# LOTR\n\nThe book rocks.", None),
    ("The Cat in the Hat", "1957-03-12", "cool book", "# The Cat in the Hat\n\n- item one\n- item two\n", 61),
    ("The Lorax", "1971-07-23", "cool book, cool film", "# The Lorax\n\n## The Lorax\n\n### The Lorax", 64)
]

genres = [
    ("Fantasy", "knights, dragons, magic, all those cool stuffs."),
    ("Children", "bedtime stories for kids I guess.")
]

bookauthors = [
    ("The Hobbit", "J. R. R. Tolkein"),
    ("The Lord of the Rings", "J. R. R. Tolkein"),
    ("The Cat in the Hat", "Dr. Seuss"),
    ("The Lorax", "Dr. Seuss")
]

bookgenres = [
    ("The Hobbit", "Fantasy"),
    ("The Lord of the Rings", "Fantasy"),
    ("The Cat in the Hat", "Children"),
    ("The Lorax", "Children")
]


def make_authors(lst):
    for i in lst:
        x = m.Author.objects.create(name=i[0], birth=i[1], death=i[2], description=i[3])
        x.save()
        print(x)


def make_books(lst):
    for i in lst:
        x = m.Book.objects.create(title=i[0], published_date=i[1], short_description=i[2], long_description=i[3], length=i[4])
        x.save()
        print(x)


def make_genres(lst):
    for i in lst:
        x = m.Genre.objects.create(name=i[0], tagline=i[1])
        x.save()
        print(x)


def make_links(books):
    lst = m.Book.objects.all()
    for i in books:
        for j in lst:
            if i[0] == j.title:
                l = m.Link.objects.create(name=f"{j.id}: TEST", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                l.save()
                bl = m.BookLink.objects.create(book=j, link=l)
                bl.save()
                print(l, bl)


def make_bookauthors(lst):
    books = m.Book.objects.all()
    authors = m.Author.objects.all()

    for i in lst:
        for j in books:
            for k in authors:
                if i[0] == j.title and i[1] == k.name:
                    x = m.BookAuthor.objects.create(book=j, author=k)
                    x.save()
                    print(x)


def make_bookgenres(lst):
    books = m.Book.objects.all()
    genres = m.Genre.objects.all()

    for i in lst:
        for j in books:
            for k in genres:
                if i[0] == j.title and i[1] == k.name:
                    x = m.BookGenre.objects.create(book=j, genre=k)
                    x.save()
                    print(x)

def main():
    make_authors(authors)
    print("### AUTHORS FINISHED ###")

    make_books(books)
    print("### BOOKS FINISHED ###")

    make_genres(genres)
    print("### GENRES FINISHED ###")

    make_links(books)
    print("### LINKS FINISHED ###")

    make_bookauthors(bookauthors)
    print("### BOOKAUTHORS FINISHED ###")

    make_bookgenres(bookgenres)
    print("### BOOKGENRES FINISHED ###")