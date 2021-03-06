from database.entities.Age import Age


class Book:

    def __init__(self, book_id: int, title: str, uri: str, age: Age,
                 author: str, author_slug: str):
        self.__id = book_id
        self.__title = title
        self.__content = None
        self.__uri = uri
        self.__age = age
        self.__author = author
        self.__author_slug = author_slug

    def get_id(self) -> int:
        return self.__id

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str) -> None:
        self.__title = title

    def set_content(self, text: str) -> None:
        self.__content = text

    def get_content(self) -> str:
        return self.__content

    def get_uri(self) -> str:
        return self.__uri

    def get_age(self) -> Age:
        return self.__age

    def get_author(self) -> str:
        return self.__author

    def set_author(self, name: str):
        self.__author = name

    def get_author_slug(self) -> str:
        return self.__author_slug

    def set_author_slug(self, slug: str):
        self.__author_slug = slug

    def set_age(self, age: Age):
        self.__age = age

    def __str__(self):
        id = str(self.get_id()) if self.get_id() else ''
        title = self.get_title() if self.get_title() else ''
        has_content = 'True' if self.get_content() is not None else 'False'
        uri = self.get_uri() if self.get_uri() else ''
        age = str(self.get_age()) if self.get_age() else ''
        author = str(self.get_author()) if self.get_author() else ''

        return '(' + id + ', ' + title + ', has_content: ' + has_content + ', ' + uri + ', ' + age + ', ' + author + ')'
