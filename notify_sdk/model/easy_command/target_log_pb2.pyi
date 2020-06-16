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

from notify_sdk.model.easy_command.action_log_pb2 import (
    ActionLog as notify_sdk___model___easy_command___action_log_pb2___ActionLog,
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


class TargetLog(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text
    status = ... # type: typing___Text
    sysStatus = ... # type: typing___Text
    code = ... # type: builtin___int
    msg = ... # type: typing___Text
    usedTime = ... # type: builtin___int
    startTime = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    endTime = ... # type: typing___Text

    @property
    def actionsLog(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[notify_sdk___model___easy_command___action_log_pb2___ActionLog]: ...

    def __init__(self,
        *,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        sysStatus : typing___Optional[typing___Text] = None,
        code : typing___Optional[builtin___int] = None,
        msg : typing___Optional[typing___Text] = None,
        actionsLog : typing___Optional[typing___Iterable[notify_sdk___model___easy_command___action_log_pb2___ActionLog]] = None,
        usedTime : typing___Optional[builtin___int] = None,
        startTime : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetLog: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetLog: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actionsLog",b"actionsLog",u"code",b"code",u"endTime",b"endTime",u"msg",b"msg",u"startTime",b"startTime",u"status",b"status",u"sysStatus",b"sysStatus",u"targetId",b"targetId",u"targetName",b"targetName",u"updateTime",b"updateTime",u"usedTime",b"usedTime"]) -> None: ...
