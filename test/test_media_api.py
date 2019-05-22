# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest,time

import openadk
from openadk.api.media_api import MediaApi  # noqa: E501
from openadk.rest import ApiException


class TestMediaApi(unittest.TestCase):
    """MediaApi unit test stubs"""

    def setUp(self):
        self.configuration = openadk.Configuration()
        self.configuration.host = 'http://10.10.69.146:9090/v1'
        self.api_instance = openadk.api.media_api.MediaApi(openadk.ApiClient(self.configuration))  # noqa: E501
    def tearDown(self):
        pass

    def test_delete_media_music(self):
        """Test case for delete_media_music

        Delete uploaded music  # noqa: E501
        """
        body = openadk.Name('test_motion')  # Name | 音乐文件名

        try:
            # 删除音乐文件（只能删除用户上传的文件）
            api_response = self.api_instance.delete_media_music(body)
            print(api_response)
            self.assertIn(api_response.code, (0, 120))
        except ApiException as e:
            print("Exception when calling MediaApi->delete_media_music: %s\n" % e)

    def test_get_media_music(self):
        """Test case for get_media_music

        Get the music playing status  # noqa: E501
        """
        try:
            # 获取音乐播放状态
            api_response = self.api_instance.get_media_music()
            print(api_response)
            self.assertEqual(0, api_response.code)
        except ApiException as e:
            print("Exception when calling MediaApi->get_media_music: %s\n" % e)

    def test_get_media_music_list(self):
        """Test case for get_media_music_list

        Get the music list  # noqa: E501
        """
        try:
            # 获取音乐列表
            api_response = self.api_instance.get_media_music_list()
            print(api_response)
            self.assertEqual(0, api_response.code)
            self.assertNotEqual(None, api_response.data)
        except ApiException as e:
            print("Exception when calling MediaApi->get_media_music_list: %s\n" % e)

    def test_post_media_music(self):
        """Test case for post_media_music

        Upload music  # noqa: E501
        """
        for name in ['test_motion.hts', 'test_motion.mp3', 'test_motion.zip']:
            file = 'res_motions/'+name  # file | 上传文件
            try:
                # 上传音乐文件
                api_response = self.api_instance.post_media_music(file)
                print(api_response)
                if file.endswith('mp3') or file.endswith('wav'):
                    self.assertEqual(0, api_response.code)
                else:
                    self.assertEqual(121, api_response.code)
            except ApiException as e:
                print("Exception when calling MediaApi->post_media_music: %s\n" % e)

    def test_put_media_music(self):
        """Test case for put_media_music

        Start or stop music  # noqa: E501
        """
        for operation in ['start', 'stop']:
            body = openadk.MediaMusicOperation(operation=operation)  # MediaMusicOperation | 音乐播放控制
            try:
                # 播放/停止音乐
                api_response = self.api_instance.put_media_music(body)
                print(api_response)
                self.assertEqual(0, api_response.code)
                self.assertNotEqual(None, api_response.data)
                if operation == 'start':
                    time.sleep(3)
            except ApiException as e:
                print("Exception when calling MediaApi->put_media_music: %s\n" % e)


if __name__ == '__main__':
    unittest.main()
