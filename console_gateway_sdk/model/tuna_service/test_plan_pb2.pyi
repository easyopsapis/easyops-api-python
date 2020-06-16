# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from console_gateway_sdk.model.tuna_service.requirement_instance_pb2 import (
    RequirementInstance as console_gateway_sdk___model___tuna_service___requirement_instance_pb2___RequirementInstance,
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


class TestPlan(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    reviewDate = ... # type: typing___Text
    startExcutePlanDate = ... # type: typing___Text
    projectStartDate = ... # type: typing___Text
    projectPlanCompleteDate = ... # type: typing___Text
    projectActualCompleteDate = ... # type: typing___Text
    functionMissCount = ... # type: builtin___int
    backendBugCount = ... # type: builtin___int
    bugPercent = ... # type: typing___Text
    bugTotal = ... # type: builtin___int
    capabilityCount = ... # type: builtin___int
    codingErrCount = ... # type: builtin___int
    delayPercent = ... # type: typing___Text
    environmentCount = ... # type: builtin___int
    frontBugCount = ... # type: builtin___int
    projectScore = ... # type: typing___Text
    requirementBlurryCount = ... # type: builtin___int
    scenarioBugCount = ... # type: builtin___int
    scenarioCount = ... # type: builtin___int
    status = ... # type: typing___Text
    suggestionCount = ... # type: builtin___int
    unableAppearCount = ... # type: builtin___int

    @property
    def requirement_instance(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[console_gateway_sdk___model___tuna_service___requirement_instance_pb2___RequirementInstance]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        reviewDate : typing___Optional[typing___Text] = None,
        startExcutePlanDate : typing___Optional[typing___Text] = None,
        projectStartDate : typing___Optional[typing___Text] = None,
        projectPlanCompleteDate : typing___Optional[typing___Text] = None,
        projectActualCompleteDate : typing___Optional[typing___Text] = None,
        functionMissCount : typing___Optional[builtin___int] = None,
        backendBugCount : typing___Optional[builtin___int] = None,
        bugPercent : typing___Optional[typing___Text] = None,
        bugTotal : typing___Optional[builtin___int] = None,
        capabilityCount : typing___Optional[builtin___int] = None,
        codingErrCount : typing___Optional[builtin___int] = None,
        delayPercent : typing___Optional[typing___Text] = None,
        environmentCount : typing___Optional[builtin___int] = None,
        frontBugCount : typing___Optional[builtin___int] = None,
        projectScore : typing___Optional[typing___Text] = None,
        requirementBlurryCount : typing___Optional[builtin___int] = None,
        scenarioBugCount : typing___Optional[builtin___int] = None,
        scenarioCount : typing___Optional[builtin___int] = None,
        status : typing___Optional[typing___Text] = None,
        suggestionCount : typing___Optional[builtin___int] = None,
        unableAppearCount : typing___Optional[builtin___int] = None,
        requirement_instance : typing___Optional[typing___Iterable[console_gateway_sdk___model___tuna_service___requirement_instance_pb2___RequirementInstance]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TestPlan: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TestPlan: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"backendBugCount",b"backendBugCount",u"bugPercent",b"bugPercent",u"bugTotal",b"bugTotal",u"capabilityCount",b"capabilityCount",u"codingErrCount",b"codingErrCount",u"delayPercent",b"delayPercent",u"environmentCount",b"environmentCount",u"frontBugCount",b"frontBugCount",u"functionMissCount",b"functionMissCount",u"instanceId",b"instanceId",u"name",b"name",u"projectActualCompleteDate",b"projectActualCompleteDate",u"projectPlanCompleteDate",b"projectPlanCompleteDate",u"projectScore",b"projectScore",u"projectStartDate",b"projectStartDate",u"requirementBlurryCount",b"requirementBlurryCount",u"requirement_instance",b"requirement_instance",u"reviewDate",b"reviewDate",u"scenarioBugCount",b"scenarioBugCount",u"scenarioCount",b"scenarioCount",u"startExcutePlanDate",b"startExcutePlanDate",u"status",b"status",u"suggestionCount",b"suggestionCount",u"unableAppearCount",b"unableAppearCount"]) -> None: ...
