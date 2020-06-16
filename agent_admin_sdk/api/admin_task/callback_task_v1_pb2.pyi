# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from agent_admin_sdk.model.easy_command.target_log_pb2 import (
    TargetLog as agent_admin_sdk___model___easy_command___target_log_pb2___TargetLog,
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


class CallbackAdminTaskV1Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    taskId = ... # type: typing___Text
    status = ... # type: typing___Text
    code = ... # type: builtin___int
    name = ... # type: typing___Text

    @property
    def targetsLog(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[agent_admin_sdk___model___easy_command___target_log_pb2___TargetLog]: ...

    def __init__(self,
        *,
        taskId : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        code : typing___Optional[builtin___int] = None,
        targetsLog : typing___Optional[typing___Iterable[agent_admin_sdk___model___easy_command___target_log_pb2___TargetLog]] = None,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CallbackAdminTaskV1Request: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CallbackAdminTaskV1Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"name",b"name",u"status",b"status",u"targetsLog",b"targetsLog",u"taskId",b"taskId"]) -> None: ...

class CallbackAdminTaskV1Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    status = ... # type: typing___Text

    def __init__(self,
        *,
        status : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CallbackAdminTaskV1Response: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CallbackAdminTaskV1Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"status",b"status"]) -> None: ...

class CallbackAdminTaskV1ResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CallbackAdminTaskV1Response: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CallbackAdminTaskV1Response] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CallbackAdminTaskV1ResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CallbackAdminTaskV1ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
