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

from resource_monitor_sdk.model.health_assessment.health_assessment_related_resource_event_score_pb2 import (
    HealthAssessmentRelatedResourceEventScore as resource_monitor_sdk___model___health_assessment___health_assessment_related_resource_event_score_pb2___HealthAssessmentRelatedResourceEventScore,
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


class GetCloselyHealthAssessmentResultByTimestampRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    timestamp = ... # type: builtin___int

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        timestamp : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetCloselyHealthAssessmentResultByTimestampRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetCloselyHealthAssessmentResultByTimestampRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"objectId",b"objectId",u"timestamp",b"timestamp"]) -> None: ...

class GetCloselyHealthAssessmentResultByTimestampResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    ruleId = ... # type: typing___Text
    ruleVersionId = ... # type: typing___Text
    objectId = ... # type: typing___Text
    eventScore = ... # type: builtin___int
    relationScore = ... # type: builtin___int
    healthScore = ... # type: builtin___int
    eventScoreWeight = ... # type: builtin___int
    relatedResourceWeight = ... # type: builtin___int
    timestamp = ... # type: builtin___int

    @property
    def relatedResourceEventScores(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_monitor_sdk___model___health_assessment___health_assessment_related_resource_event_score_pb2___HealthAssessmentRelatedResourceEventScore]: ...

    @property
    def eventScoreConfig(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_monitor_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        ruleId : typing___Optional[typing___Text] = None,
        ruleVersionId : typing___Optional[typing___Text] = None,
        objectId : typing___Optional[typing___Text] = None,
        eventScore : typing___Optional[builtin___int] = None,
        relationScore : typing___Optional[builtin___int] = None,
        healthScore : typing___Optional[builtin___int] = None,
        relatedResourceEventScores : typing___Optional[typing___Iterable[resource_monitor_sdk___model___health_assessment___health_assessment_related_resource_event_score_pb2___HealthAssessmentRelatedResourceEventScore]] = None,
        eventScoreWeight : typing___Optional[builtin___int] = None,
        relatedResourceWeight : typing___Optional[builtin___int] = None,
        timestamp : typing___Optional[builtin___int] = None,
        eventScoreConfig : typing___Optional[typing___Iterable[resource_monitor_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetCloselyHealthAssessmentResultByTimestampResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetCloselyHealthAssessmentResultByTimestampResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"eventScore",b"eventScore",u"eventScoreConfig",b"eventScoreConfig",u"eventScoreWeight",b"eventScoreWeight",u"healthScore",b"healthScore",u"instanceId",b"instanceId",u"objectId",b"objectId",u"relatedResourceEventScores",b"relatedResourceEventScores",u"relatedResourceWeight",b"relatedResourceWeight",u"relationScore",b"relationScore",u"ruleId",b"ruleId",u"ruleVersionId",b"ruleVersionId",u"timestamp",b"timestamp"]) -> None: ...

class GetCloselyHealthAssessmentResultByTimestampResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetCloselyHealthAssessmentResultByTimestampResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetCloselyHealthAssessmentResultByTimestampResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetCloselyHealthAssessmentResultByTimestampResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetCloselyHealthAssessmentResultByTimestampResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
