from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Note
from blog_api import filters


class TestBlogAPINoteFilters(TestCase):
    @classmethod
    def setUpTestData(cls):

        test_user_1 = User(
            username="test_user_1",
            password="fake_password"
        )
        test_user_2 = User(
            username="test_user_2",
            password="fake_password"
        )
        test_user_1, test_user_2 = User.objects.bulk_create(
            [test_user_1, test_user_2]
        )

        Note(title="title_1", author=test_user_1).save()
        Note(title="title_3", author=test_user_1).save()
        Note(title="title_2", author_id=test_user_2.id).save()

    def test_note_filter_by_author_id(self):

        queryset = Note.objects.all()
        filter_author_id = 1

        expected_queryset = queryset.filter(author_id=filter_author_id)
        actual_filter = filters.note_filter_by_author_id(
            queryset,
            author_id=filter_author_id,
        )

        self.assertQuerysetEqual(actual_filter, expected_queryset, ordered=False)

    # def test_filter(self):
    #     Note.objects.filter(author__username=...)
    #     Note.objects.filter(author__date_joined__year__gte=...)
