import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2
    
    @pytest.mark.parametrize('name, genre',[['Начало', 'Фантастика'], ['В парке', 'Детективы'], ['Ночь', 'Ужасы']])
    def test_set_book_genre_different(self, name, genre):
         collector = BooksCollector()
         collector.add_new_book(name)
         collector.set_book_genre(name, genre)
         assert collector.books_genre[name] == genre


    def test_set_book_genre_no_genre(self):
         collector = BooksCollector()
         collector.add_new_book('Начало')
         collector.set_book_genre('Начало', '')
         collector.add_new_book('Я сама')
         collector.set_book_genre('Я сама', 'Автобиография')
         assert len(collector.books_genre) == 2 and collector.books_genre['Я сама'] == '' and collector.books_genre['Начало'] == ''
         
    @pytest.mark.parametrize('name, genre',[['Начало', 'Фантастика'], ['В парке', 'Детективы'], ['Ночь', 'Ужасы']])
    def  test_get_book_genre(self, name, genre):
         collector = BooksCollector()
         collector.add_new_book(name)
         collector.set_book_genre(name, genre)
         assert collector.get_book_genre(name) == genre

   
    def test_get_books_with_specific_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Начало')
        collector.set_book_genre('Начало', 'Фантастика')
        collector.add_new_book('Ночь')
        collector.set_book_genre('Ночь', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы')[0] == 'Ночь' and  len(collector.get_books_with_specific_genre('Ужасы')) == 1



    def test_get_books_for_children_true(self):
        collector = BooksCollector()
        collector.add_new_book('Улица')
        collector.set_book_genre('Улица', 'Детективы')
        collector.add_new_book('Ночь')
        collector.set_book_genre('Ночь', 'Ужасы')
        collector.add_new_book('Алиса в стране чудес')
        collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
        collector.add_new_book('Стена')
        collector.set_book_genre('Стена', 'Фантастика')
        assert 'Стена' in collector.get_books_for_children() and 'Алиса в стране чудес' in collector.get_books_for_children() and  len(collector.get_books_for_children()) == 2


    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Ночь')
        collector.set_book_genre('Ночь', 'Ужасы')
        collector.add_book_in_favorites('Ночь')
        assert collector.favorites[0] == 'Ночь' and len( collector.favorites) == 1


    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Ночь')
        collector.set_book_genre('Ночь', 'Ужасы')
        collector.add_new_book('Алиса в стране чудес')
        collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
        collector.add_book_in_favorites('Ночь')
        collector.add_book_in_favorites('Алиса в стране чудес')
        collector.delete_book_from_favorites('Ночь')
        assert collector.favorites[0] == 'Алиса в стране чудес' and len( collector.favorites) == 1


    def test_get_list_of_favorites_books_true(self):
         collector = BooksCollector()
         collector.add_new_book('Ночь')
         collector.set_book_genre('Ночь', 'Ужасы')
         collector.add_new_book('Алиса в стране чудес')
         collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
         collector.add_book_in_favorites('Ночь')
         collector.add_book_in_favorites('Алиса в стране чудес')
         assert 'Ночь' in collector.get_list_of_favorites_books() and 'Алиса в стране чудес' in collector.get_list_of_favorites_books() and len(collector.get_list_of_favorites_books()) == 2 

         
         
    def test_get_books_genre(self):
         collector = BooksCollector()
         collector.add_new_book('Ночь')
         collector.set_book_genre('Ночь', 'Ужасы')
         collector.add_new_book('Алиса в стране чудес')
         collector.set_book_genre('Алиса в стране чудес', 'Мультфильмы')
         collector.add_book_in_favorites('Ночь')
         collector.add_book_in_favorites('Алиса в стране чудес')
         assert collector.get_books_genre()['Ночь'] == 'Ужасы' and collector.get_books_genre()['Алиса в стране чудес'] == 'Мультфильмы' and len(collector.get_books_genre())==2
