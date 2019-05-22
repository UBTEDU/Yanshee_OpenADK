# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest
from pprint import pprint

import openadk
from openadk.models.visions_stream import VisionsStream  # noqa: E501
from openadk.rest import ApiException


class TestVisionsStream(unittest.TestCase):
    """VisionsStream unit test stubs"""

    def setUp(self):
        self.configuration = openadk.Configuration()
        self.configuration.host = 'http://10.10.60.196:9090/v1'
        self.api_instance = openadk.api.visions_api.VisionsApi(openadk.ApiClient(self.configuration))  # noqa: E501
        pass

    def tearDown(self):
        pass

    def testVisionsStream(self):
        """Test VisionsStream"""
        # FIXME: construct object with mandatory attributes with example values
        body = openadk.VisionsStream(resolution='640x480')  # VisionsStream |  (optional)

        for i in range(1):
            try:
                # 打开摄像头的视频流
                api_response = self.api_instance.post_visions_streams(body=body)
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling VisionsApi->post_visions_streams: %s\n" % e)

            try:
                # 关闭摄像头的视频流
                api_response = self.api_instance.delete_visions_streams()
                pprint(api_response)
            except ApiException as e:
                print("Exception when calling VisionsApi->delete_visions_streams: %s\n" % e)


if __name__ == '__main__':
    unittest.main()
