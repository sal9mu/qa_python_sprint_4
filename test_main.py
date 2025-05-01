from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book(self, collector):
        collector.add_new_book("Гарри Поттер")
        assert "Гарри Поттер" in collector.get_books_genre()

    def test_set_book_genre(self, collector):
        self.book = "Дюна"
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, "Фантастика")
        assert collector.get_book_genre(self.book) == "Фантастика"

    def test_get_book_genre(self, collector):
        self.book = "Властелин колец"
        collector.add_new_book(self.book)
        collector.set_book_genre(self.book, "Фантастика")
        assert collector.get_book_genre(self.book) == "Фантастика"

    def test_get_books_with_specific_genre(self, books_list, collector):
        for book, genre in books_list.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert "Гарри Поттер" in collector.get_books_with_specific_genre("Фантастика")

    def test_add_book_in_favorites(self, collector):
        self.book = 'Иллидан'
        collector.add_new_book(self.book)
        collector.add_book_in_favorites(self.book)
        assert self.book in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorite(self, collector):
        self.book = 'Сильмариллион'
        collector.add_new_book(self.book)
        collector.add_book_in_favorites(self.book)
        assert self.book in collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites(self.book)
        assert self.book not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector, books_list):
        for book, genre in books_list.items():
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        favorites = collector.get_list_of_favorites_books()
        assert set(favorites) == set(books_list.keys())

    def test_get_books_for_children(self, collector, books_list):
        for book, genre in books_list.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        children_books = collector.get_books_for_children()
        expected_children_books = ["Гарри Поттер", "Маша и медведь", "Двенадцать стульев"]
        assert sorted(children_books) == sorted(expected_children_books)

    def test_get_books_genre(self, collector, books_list):
        for book, genre in books_list.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        assert collector.get_books_genre() == books_list
