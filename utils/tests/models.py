"""
This module holds classes and functions to help with tests
on models.
"""
from django.db.models import Model


class TestModel:
    @classmethod
    def get_verbose_name(cls, model: Model, field: str) -> str:
        """
        Use this method to get a model fields
        verbose name

        :param model: The model to use
        :type model: Django model
        :param field: The field you want to get the verbose name of
        :type field: str
        :rtype: str
        :return: The model fields verbose name
        """
        return model._meta.get_field(field).verbose_name

    @classmethod
    def get_max_length(cls, model: Model, field: str) -> int:
        """
        Use this method to get a model fields max length

        :param model: The model to use
        :type model: Django model
        :param field: The field you want to get the max length for
        :type field: str:
        :rtype: int
        :return: The maximum length a model field will accept
        """
        return model._meta.get_field(field).max_length

    @classmethod
    def get_field(cls, model: Model, field: str) -> str:
        """
        Use this method to get a model's field

        :param model: The model to use
        :type model: Django model
        :param field: The field you want to get
        :type field: str
        :rtype: str
        :return: The model field
        """
        return model._meta.get_field(field)
