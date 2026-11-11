from django.test import TestCase
from datetime import date
from django.urls import reverse

from .models import Author, Book


class ProjectURLTests(TestCase):
    def test_project_includes_app_urls_without_recursive_include(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class BookRelationshipTests(TestCase):
    def test_book_uses_an_author_instance(self):
        author = Author.objects.create(
            name='abce',
            email='author@example.com',
            description='Book author',
        )
        book = Book.objects.create(
            title='hero',
            author=author,
            published_date=date(2003, 3, 24),
            isbn='9780000000002',
            pages=200,
            cover_image='book_covers/hero.jpg',
            language='English',
        )

        self.assertEqual(book.author, author)
        self.assertEqual(Book.objects.get(pk=book.pk).author.name, 'abce')


class URLTests(TestCase):
    def test_sampletest_url(self):
        response = self.client.get('/sampletest/')
        self.assertEqual(response.status_code, 200)
    
    def test_sampletest_content(self):
        response = self.client.get('/sampletest/')
        self.assertContains(response, "This is a sample test page.")
    def test_sampletest_negativeurl(self):
        response = self.client.get('/newsampletest/')
        self.assertEqual(response.status_code, 404)
    def test_sampletest_urlname(self):
        url =reverse('st')
        response =self.client.get(url)
        self.assertEqual(response.status_code,200)


        def test_sampletest1_parameter(self):
            url=reverse('st1',args=[23])
            response =self.client.get(url)
            self.assertContains(response,23) #here if anyother number it will say failed ex = 24,27,20 any num

        def test_home_template(self):
            response=self.client.get('/home/')
            self.assertTemplateUsed(response,'home.html')
            




