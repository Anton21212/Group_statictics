from unittest import *
from db import models


class TestPostObjsList(TestCase):
    def test_get(self):
        result = models.PostsOBJ.objects.get(count=2, offset=1)
        self.assertIsNotNone(result, "Что-то пошло не так")
        print(result)

    def test_all(self):
        result = models.PostsOBJ.objects.all()
        self.assertIsNotNone(result, "Что-то пошло не так")
        print(result)

    def test_get_by_id(self):
        result = models.PostsOBJ.objects.get_by_id(1)
        self.assertIsNotNone(result, "Что-то пошло не так")
        print(result)

    def test_create(self):
        result = models.PostsOBJ.create(date_=123123)
        self.assertIsNone(result, "НЕ None")

    def test_update(self):
        result = models.PostsOBJ.update(new_values=5555, id_=6, pols="date")
        self.assertIsNone(result, "НЕ None")

    def test_delete(self):
        result = models.PostsOBJ.delete(id_=6)
        self.assertIsNone(result, "НЕ None")


class TestGroupObjsList(TestCase):
    def test_all(self):
        result = models.GroupOBJ.objects.all()
        self.assertIsNotNone(result, "Cкорее такого идентификатора нету")
        print(result)

    def test_get_by_subsequence(self):
        result = models.GroupOBJ.objects.get_by_subsequence(subsequence=1)
        self.assertIsNotNone(result, "Cкорее такого идентификатора нету")
        print(result)

    def test_create(self):
        result = models.GroupOBJ.create(id_=4)
        self.assertIsNotNone(result, "НЕ None")

    def test_update(self):
        result = models.GroupOBJ.update(pols="id", new_values=4044, subsequence=1)
        self.assertIsNotNone(result, msg=None)

    def test_delete(self):
        result = models.GroupOBJ.delete(subsequence=3)
        self.assertIsNotNone(result, "НЕ None")
