# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
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


class TestPlanComplete(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
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
    scenarioCount = ... # type: builtin___int
    status = ... # type: typing___Text
    suggestionCount = ... # type: builtin___int
    unableAppearCount = ... # type: builtin___int

    def __init__(self,
        *,
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
        scenarioCount : typing___Optional[builtin___int] = None,
        status : typing___Optional[typing___Text] = None,
        suggestionCount : typing___Optional[builtin___int] = None,
        unableAppearCount : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TestPlanComplete: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TestPlanComplete: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"backendBugCount",b"backendBugCount",u"bugPercent",b"bugPercent",u"bugTotal",b"bugTotal",u"capabilityCount",b"capabilityCount",u"codingErrCount",b"codingErrCount",u"delayPercent",b"delayPercent",u"environmentCount",b"environmentCount",u"frontBugCount",b"frontBugCount",u"functionMissCount",b"functionMissCount",u"projectActualCompleteDate",b"projectActualCompleteDate",u"projectScore",b"projectScore",u"requirementBlurryCount",b"requirementBlurryCount",u"scenarioCount",b"scenarioCount",u"status",b"status",u"suggestionCount",b"suggestionCount",u"unableAppearCount",b"unableAppearCount"]) -> None: ...
