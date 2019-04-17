# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from openadk.models.devices_battery import DevicesBattery  # noqa: F401,E501


class DevicesBatteryResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'data': 'DevicesBattery',
        'msg': 'str'
    }

    attribute_map = {
        'code': 'code',
        'data': 'data',
        'msg': 'msg'
    }

    def __init__(self, code=None, data=None, msg=None):  # noqa: E501
        """DevicesBatteryResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._data = None
        self._msg = None
        self.discriminator = None

        self.code = code
        self.data = data
        self.msg = msg

    @property
    def code(self):
        """Gets the code of this DevicesBatteryResponse.  # noqa: E501

        返回码，0表示正常  # noqa: E501

        :return: The code of this DevicesBatteryResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DevicesBatteryResponse.

        返回码，0表示正常  # noqa: E501

        :param code: The code of this DevicesBatteryResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def data(self):
        """Gets the data of this DevicesBatteryResponse.  # noqa: E501


        :return: The data of this DevicesBatteryResponse.  # noqa: E501
        :rtype: DevicesBattery
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DevicesBatteryResponse.


        :param data: The data of this DevicesBatteryResponse.  # noqa: E501
        :type: DevicesBattery
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def msg(self):
        """Gets the msg of this DevicesBatteryResponse.  # noqa: E501

        提示信息  # noqa: E501

        :return: The msg of this DevicesBatteryResponse.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this DevicesBatteryResponse.

        提示信息  # noqa: E501

        :param msg: The msg of this DevicesBatteryResponse.  # noqa: E501
        :type: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DevicesBatteryResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DevicesBatteryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
