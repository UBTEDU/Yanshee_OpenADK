# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.subscription_name import SubscriptionName  # noqa: F401,E501
from openadk.models.subscription_visions_analysis import SubscriptionVisionsAnalysis  # noqa: F401,E501
from openadk import util


class SubscriptionVisionsResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, analysis=None, recognition=None, quantity=None, color=None):  # noqa: E501
        """SubscriptionVisionsResults - a model defined in Swagger

        :param analysis: The analysis of this SubscriptionVisionsResults.  # noqa: E501
        :type analysis: SubscriptionVisionsAnalysis
        :param recognition: The recognition of this SubscriptionVisionsResults.  # noqa: E501
        :type recognition: SubscriptionName
        :param quantity: The quantity of this SubscriptionVisionsResults.  # noqa: E501
        :type quantity: int
        :param color: The color of this SubscriptionVisionsResults.  # noqa: E501
        :type color: List[SubscriptionName]
        """
        self.swagger_types = {
            'analysis': SubscriptionVisionsAnalysis,
            'recognition': SubscriptionName,
            'quantity': int,
            'color': List[SubscriptionName]
        }

        self.attribute_map = {
            'analysis': 'analysis',
            'recognition': 'recognition',
            'quantity': 'quantity',
            'color': 'color'
        }

        self._analysis = analysis
        self._recognition = recognition
        self._quantity = quantity
        self._color = color

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionVisionsResults of this SubscriptionVisionsResults.  # noqa: E501
        :rtype: SubscriptionVisionsResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def analysis(self):
        """Gets the analysis of this SubscriptionVisionsResults.


        :return: The analysis of this SubscriptionVisionsResults.
        :rtype: SubscriptionVisionsAnalysis
        """
        return self._analysis

    @analysis.setter
    def analysis(self, analysis):
        """Sets the analysis of this SubscriptionVisionsResults.


        :param analysis: The analysis of this SubscriptionVisionsResults.
        :type analysis: SubscriptionVisionsAnalysis
        """

        self._analysis = analysis

    @property
    def recognition(self):
        """Gets the recognition of this SubscriptionVisionsResults.


        :return: The recognition of this SubscriptionVisionsResults.
        :rtype: SubscriptionName
        """
        return self._recognition

    @recognition.setter
    def recognition(self, recognition):
        """Sets the recognition of this SubscriptionVisionsResults.


        :param recognition: The recognition of this SubscriptionVisionsResults.
        :type recognition: SubscriptionName
        """

        self._recognition = recognition

    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionVisionsResults.

        Quantity.  # noqa: E501

        :return: The quantity of this SubscriptionVisionsResults.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionVisionsResults.

        Quantity.  # noqa: E501

        :param quantity: The quantity of this SubscriptionVisionsResults.
        :type quantity: int
        """
        if quantity is not None and quantity < 0:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must be a value greater than or equal to `0`")  # noqa: E501

        self._quantity = quantity

    @property
    def color(self):
        """Gets the color of this SubscriptionVisionsResults.

         The color results. The possible values: - none - black - gray - white - red - orange - yellow - green - cyan - blue - purple   # noqa: E501

        :return: The color of this SubscriptionVisionsResults.
        :rtype: List[SubscriptionName]
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this SubscriptionVisionsResults.

         The color results. The possible values: - none - black - gray - white - red - orange - yellow - green - cyan - blue - purple   # noqa: E501

        :param color: The color of this SubscriptionVisionsResults.
        :type color: List[SubscriptionName]
        """

        self._color = color
