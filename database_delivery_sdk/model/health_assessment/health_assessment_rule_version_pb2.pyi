# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from database_delivery_sdk.model.health_assessment.health_assessment_event_score_config_item_pb2 import (
    HealthAssessmentEventScoreConfigItem as database_delivery_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem,
)

from database_delivery_sdk.model.health_assessment.health_assessment_related_resource_score_config_item_pb2 import (
    HealthAssessmentRelatedResourceScoreConfigItem as database_delivery_sdk___model___health_assessment___health_assessment_related_resource_score_config_item_pb2___HealthAssessmentRelatedResourceScoreConfigItem,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
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


class HealthAssessmentRuleVersion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    ruleId = ... # type: typing___Text
    objectId = ... # type: typing___Text
    eventScoreWeight = ... # type: builtin___int
    relatedResourceWeight = ... # type: builtin___int

    @property
    def eventScoreConfig(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[database_delivery_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem]: ...

    @property
    def relatedResourceScoreConfig(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[database_delivery_sdk___model___health_assessment___health_assessment_related_resource_score_config_item_pb2___HealthAssessmentRelatedResourceScoreConfigItem]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        ruleId : typing___Optional[typing___Text] = None,
        objectId : typing___Optional[typing___Text] = None,
        eventScoreConfig : typing___Optional[typing___Iterable[database_delivery_sdk___model___health_assessment___health_assessment_event_score_config_item_pb2___HealthAssessmentEventScoreConfigItem]] = None,
        relatedResourceScoreConfig : typing___Optional[typing___Iterable[database_delivery_sdk___model___health_assessment___health_assessment_related_resource_score_config_item_pb2___HealthAssessmentRelatedResourceScoreConfigItem]] = None,
        eventScoreWeight : typing___Optional[builtin___int] = None,
        relatedResourceWeight : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> HealthAssessmentRuleVersion: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> HealthAssessmentRuleVersion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"eventScoreConfig",b"eventScoreConfig",u"eventScoreWeight",b"eventScoreWeight",u"instanceId",b"instanceId",u"objectId",b"objectId",u"relatedResourceScoreConfig",b"relatedResourceScoreConfig",u"relatedResourceWeight",b"relatedResourceWeight",u"ruleId",b"ruleId"]) -> None: ...
