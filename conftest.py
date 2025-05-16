import pytest
from main import BooksCollector  # предполагается, что класс находится в этом модуле

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def books_list():
    test_books = {
        "Гарри Поттер": "Фантастика",
        "Оно": "Ужасы",
        "Шерлок Холмс": "Детективы",
        "Маша и медведь": "Мультфильмы",
        "Двенадцать стульев": "Комедии"
    }
    return test_books