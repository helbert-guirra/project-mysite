import pytest
from blog.factories import PostFactory, UserFactory

@pytest.fixture
def post_published(db):
    return PostFactory(title='pytest with factory', status=1)

@pytest.fixture
def user(db):
    return UserFactory(username='testuser')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'
    assert post_published.status == 1

@pytest.mark.django_db
def test_post_has_author(post_published):
    assert post_published.author is not None
    assert post_published.author.username is not None

@pytest.mark.django_db
def test_create_user(user):
    assert user.username == 'testuser'
    assert user.email is not None