# from django.urls import reverse
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APITestCase, APIClient
# from .models import Post, Category
# from django.contrib.auth.models import User
#
# # Create your tests here.
# class TestCreatePost(APITestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#
#         test_category = Category.objects.create(name="test_cat")
#
#         test_user = User.objects.create_user(username="testuser", password="12345678")
#         test_user2 = User.objects.create_user(username="testuser2", password="12345678")
#
#         test_post = Post.objects.create(author_id = 1, category_id = 1, title = 'Title One', slug='title-one', detail="Testing post", status='published')
#
#         # Test post view
#     def test_post_view(self):
#         url = reverse("restapp:post_list")
#         response = self.client.get(url, format="json")
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#         # Test post create
#     def test_blog_create(self):
#         post = Post.objects.get(pk=1)
#         cat = Category.objects.get(pk=1)
#         author = f'{post.author}'
#         detail = f'{post.detail}'
#         status = f'{post.status}'
#
#         self.assertEqual(author, "testuser")
#         # self.assertEqual(cat, "undefined")
#         self.assertEqual(detail, "Testing post")
#         self.assertEqual(status, "published")
#
#         self.assertEqual(str(cat), "test_cat")
#         self.assertEqual(str(post), "Title One")
#
#     # Test post update
#
#     def test_post_update(self):
#
#         client = APIClient()
#
#         # self.test_cat = Category.objects.create(name="test_cat")
#         # self.test_user = User.objects.create_user(username="testuser", password="12345678")
#         # test_post = Post.objects.create(author_id = 1, category_id = 1, title = 'Title One', slug='title-one', detail="Testing post", status='published')
#
#         client.login(username="testuser", password="12345678")
#
#         url = reverse(("restapp:post_detail"), kwargs={"pk": 1})
#
#         response = client.put(
#             url,
#             {
#                 "author": 1,
#                 "category": 1,
#                 "title": "Python Django API Development",
#                 "detail": "Python Django API Development",
#                 "status": "published",
#                 "published": "2020-10-06T02:58:06Z"
#             }, format="json")
#
#         print(response.data)
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_user_login(self):
#
#         client = APIClient()
#
#         url = reverse("rest_framework")
#
#         response = client.post(url,
#             {
#             "username":"testuser",
#             "passwword":"12345678"
#             }, format="json")
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
