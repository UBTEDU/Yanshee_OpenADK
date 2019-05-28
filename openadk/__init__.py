# coding: utf-8

# flake8: noqa

"""
    Yanshee Open ADK

     ## Overview  Open ADK is designed for the users that they can build their own application very quickly. Open ADK provided two features: - Easy way to call API. - Easy way to receive the data from remote device.  This Python package is automatically generated by the Swagger Codegen project: - API version: 1.0.0 - Package version: 1.0.0 ## Requirements. Python 2.7 or 3.4+ ## Installation & Usage You can install Open ADK from github. ``` pip install git+https://github.com/UBTEDU/Yanshee_OpenADK.git ``` (you may need to run pip with root permission: sudo pip install git+https://github.com//.git) Then import the package: ``` import openadk ``` ## Setuptools Install via [Setuptools](https://pypi.org/project/setuptools/). ``` python setup.py install --user ``` (or sudo python setup.py install to install the package for all users) Then import the package: ``` import openadk ``` ## Getting Started Please follow the installation procedure and then run the following: ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://<ip>:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration))  try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s \" % e) ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from openadk.api.devices_api import DevicesApi
from openadk.api.media_api import MediaApi
from openadk.api.motions_api import MotionsApi
from openadk.api.sensors_api import SensorsApi
from openadk.api.servos_api import ServosApi
from openadk.api.subscriptions_api import SubscriptionsApi
from openadk.api.visions_api import VisionsApi
from openadk.api.voice_api import VoiceApi

# import ApiClient
from openadk.api_client import ApiClient
from openadk.configuration import Configuration
# import models into sdk package
from openadk.models.common_response import CommonResponse
from openadk.models.devices_battery import DevicesBattery
from openadk.models.devices_battery_response import DevicesBatteryResponse
from openadk.models.devices_fall_management import DevicesFallManagement
from openadk.models.devices_fall_management_response import DevicesFallManagementResponse
from openadk.models.devices_led import DevicesLED
from openadk.models.devices_led_response import DevicesLEDResponse
from openadk.models.devices_language import DevicesLanguage
from openadk.models.devices_language_response import DevicesLanguageResponse
from openadk.models.devices_versions import DevicesVersions
from openadk.models.devices_versions_response import DevicesVersionsResponse
from openadk.models.devices_volume import DevicesVolume
from openadk.models.devices_volume_response import DevicesVolumeResponse
from openadk.models.media_music_list import MediaMusicList
from openadk.models.media_music_list_response import MediaMusicListResponse
from openadk.models.media_music_operation import MediaMusicOperation
from openadk.models.media_music_status import MediaMusicStatus
from openadk.models.media_music_status_response import MediaMusicStatusResponse
from openadk.models.motions_info import MotionsInfo
from openadk.models.motions_list import MotionsList
from openadk.models.motions_list_response import MotionsListResponse
from openadk.models.motions_operation import MotionsOperation
from openadk.models.motions_parameter import MotionsParameter
from openadk.models.motions_status import MotionsStatus
from openadk.models.motions_status_response import MotionsStatusResponse
from openadk.models.name import Name
from openadk.models.runtime_response import RuntimeResponse
from openadk.models.sensors_environment_info import SensorsEnvironmentInfo
from openadk.models.sensors_environment_value import SensorsEnvironmentValue
from openadk.models.sensors_environment_value_response import SensorsEnvironmentValueResponse
from openadk.models.sensors_gyro_info import SensorsGyroInfo
from openadk.models.sensors_gyro_value import SensorsGyroValue
from openadk.models.sensors_gyro_value_response import SensorsGyroValueResponse
from openadk.models.sensors_info import SensorsInfo
from openadk.models.sensors_infrared_info import SensorsInfraredInfo
from openadk.models.sensors_infrared_value import SensorsInfraredValue
from openadk.models.sensors_infrared_value_response import SensorsInfraredValueResponse
from openadk.models.sensors_list import SensorsList
from openadk.models.sensors_list_response import SensorsListResponse
from openadk.models.sensors_operation_request import SensorsOperationRequest
from openadk.models.sensors_parameter import SensorsParameter
from openadk.models.sensors_pressure_info import SensorsPressureInfo
from openadk.models.sensors_pressure_value import SensorsPressureValue
from openadk.models.sensors_pressure_value_response import SensorsPressureValueResponse
from openadk.models.sensors_touch_info import SensorsTouchInfo
from openadk.models.sensors_touch_value import SensorsTouchValue
from openadk.models.sensors_touch_value_response import SensorsTouchValueResponse
from openadk.models.sensors_ultrasonic_info import SensorsUltrasonicInfo
from openadk.models.sensors_ultrasonic_value import SensorsUltrasonicValue
from openadk.models.sensors_ultrasonic_value_response import SensorsUltrasonicValueResponse
from openadk.models.servos_angles import ServosAngles
from openadk.models.servos_angles_request import ServosAnglesRequest
from openadk.models.servos_angles_response import ServosAnglesResponse
from openadk.models.servos_list import ServosList
from openadk.models.servos_mode import ServosMode
from openadk.models.servos_mode_request import ServosModeRequest
from openadk.models.servos_mode_response import ServosModeResponse
from openadk.models.servos_result import ServosResult
from openadk.models.servos_result_response import ServosResultResponse
from openadk.models.subscriptions_asr_voice import SubscriptionsAsrVoice
from openadk.models.subscriptions_asr_voice_delete import SubscriptionsAsrVoiceDelete
from openadk.models.subscriptions_iat_voice import SubscriptionsIatVoice
from openadk.models.subscriptions_iat_voice_delete import SubscriptionsIatVoiceDelete
from openadk.models.subscriptions_motions import SubscriptionsMotions
from openadk.models.subscriptions_motions_delete import SubscriptionsMotionsDelete
from openadk.models.subscriptions_sensors import SubscriptionsSensors
from openadk.models.subscriptions_sensors_delete import SubscriptionsSensorsDelete
from openadk.models.subscriptions_tts_voice import SubscriptionsTtsVoice
from openadk.models.subscriptions_tts_voice_delete import SubscriptionsTtsVoiceDelete
from openadk.models.subscriptions_visions import SubscriptionsVisions
from openadk.models.subscriptions_visions_delete import SubscriptionsVisionsDelete
from openadk.models.total_time import TotalTime
from openadk.models.visions_analysis import VisionsAnalysis
from openadk.models.visions_delete_tags import VisionsDeleteTags
from openadk.models.visions_get_response import VisionsGetResponse
from openadk.models.visions_photo import VisionsPhoto
from openadk.models.visions_photo_list_response import VisionsPhotoListResponse
from openadk.models.visions_photo_response import VisionsPhotoResponse
from openadk.models.visions_put import VisionsPut
from openadk.models.visions_put_response import VisionsPutResponse
from openadk.models.visions_put_tags import VisionsPutTags
from openadk.models.visions_quantity import VisionsQuantity
from openadk.models.visions_results import VisionsResults
from openadk.models.visions_stream import VisionsStream
from openadk.models.visions_tags_response import VisionsTagsResponse
from openadk.models.visions_task import VisionsTask
from openadk.models.voice_asr_option import VoiceAsrOption
from openadk.models.voice_delete_offline_syntax import VoiceDeleteOfflineSyntax
from openadk.models.voice_get_offline_syntax_grammars_response import VoiceGetOfflineSyntaxGrammarsResponse
from openadk.models.voice_get_offline_syntax_response import VoiceGetOfflineSyntaxResponse
from openadk.models.voice_get_response import VoiceGetResponse
from openadk.models.voice_iat_request import VoiceIatRequest
from openadk.models.voice_offline_slot import VoiceOfflineSlot
from openadk.models.voice_offline_syntax_rule import VoiceOfflineSyntaxRule
from openadk.models.voice_post_offline_syntax import VoicePostOfflineSyntax
from openadk.models.voice_put_offline_syntax import VoicePutOfflineSyntax
from openadk.models.voice_response import VoiceResponse
from openadk.models.voice_tts_str import VoiceTTSStr
