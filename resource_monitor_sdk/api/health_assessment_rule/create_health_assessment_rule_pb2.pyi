# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from resource_monitor_sdk.model.health_assessment.health_assessment_event_score_config_item_pb2 import (
    HealthAssessmentEventScoreConfigItem as resource_monitor_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem,
)

from resource_monitor_sdk.model.health_assessment.health_assessment_related_resource_score_config_item_pb2 import (
    HealthAssessmentRelatedResourceScoreConfigItem as resource_monitor_sdk___model___health_assessment___health_assessment_related_resource_score_config_item_pb2___HealthAssessmentRelatedResourceScoreConfigItem,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class CreateHealthAssessmentRuleRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    name = ... # type: typing___Text
    eventScoreWeight = ... # type: builtin___int
    relatedResourceWeight = ... # type: builtin___int

    @property
    def eventScoreConfig(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_monitor_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem]: ...

    @property
    def relatedResourceScoreConfig(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_monitor_sdk___model___health_assessment___health_assessment_related_resource_score_config_item_pb2___HealthAssessmentRelatedResourceScoreConfigItem]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        eventScoreConfig : typing___Optional[typing___Iterable[resource_monitor_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem]] = None,
        relatedResourceScoreConfig : typing___Optional[typing___Iterable[resource_monitor_sdk___model___health_assessment___health_assessment_related_resource_score_config_item_pb2___HealthAssessmentRelatedResourceScoreConfigItem]] = None,
        eventScoreWeight : typing___Optional[builtin___int] = None,
        relatedResourceWeight : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateHealthAssessmentRuleRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateHealthAssessmentRuleRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"eventScoreConfig",b"eventScoreConfig",u"eventScoreWeight",b"eventScoreWeight",u"name",b"name",u"objectId",b"objectId",u"relatedResourceScoreConfig",b"relatedResourceScoreConfig",u"relatedResourceWeight",b"relatedResourceWeight"]) -> None: ...

class CreateHealthAssessmentRuleResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateHealthAssessmentRuleResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateHealthAssessmentRuleResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> None: ...

class CreateHealthAssessmentRuleResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CreateHealthAssessmentRuleResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CreateHealthAssessmentRuleResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateHealthAssessmentRuleResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateHealthAssessmentRuleResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
