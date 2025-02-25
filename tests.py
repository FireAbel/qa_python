import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста написан неправильно и вызывает ошибку, поэтому исправляю его
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.mark.parametrize("book_name", ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби', 'Полярный экспресс'])
    def test_add_new_book_add_books(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_add_genre_to_the_book(self):
        collector = BooksCollector()
        collector.add_new_book('Просперо в огне')
        collector.set_book_genre('Просперо в огне', 'Фантастика')
        assert collector.get_book_genre('Просперо в огне') == 'Фантастика'

    def test_get_book_genre_outputs_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Просперо в огне')
        collector.set_book_genre('Просперо в огне', 'Фантастика')
        assert collector.get_book_genre('Просперо в огне') == 'Фантастика'

    def test_get_books_with_specific_genre_return_a_list_of_books(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Антиутопия')
        collector.add_new_book('Просперо в огне')
        collector.set_book_genre('Просперо в огне', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Просперо в огне']

    def test_get_books_genre_return_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        expected_genre = {
            '1984': 'Фантастика',
            'Сияние': 'Ужасы'
        }
        assert collector.get_books_genre() == expected_genre

    def test_get_books_for_children_return_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Кладбище домашних животных')
        collector.set_book_genre('Кладбище домашних животных', 'Ужасы')
        assert collector.get_books_for_children() == ['Гарри Поттер']

    def test_add_book_in_favorites_books_added_in_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_deleted_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize("book_name", ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби',
                              'Полярный экспресс'])
    def test_favorites_list_retrieved_return_favorites_list(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == [book_name]
