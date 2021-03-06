# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.empty_pb2 import (
    Empty as google___protobuf___empty_pb2___Empty,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from terraform_sdk.model.cmdb.tf_lock_info_pb2 import (
    TFLockInfo as terraform_sdk___model___cmdb___tf_lock_info_pb2___TFLockInfo,
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


class LockStateRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    tfId = ... # type: typing___Text
    org = ... # type: typing___Text
    user = ... # type: typing___Text

    @property
    def body(self) -> terraform_sdk___model___cmdb___tf_lock_info_pb2___TFLockInfo: ...

    def __init__(self,
        *,
        tfId : typing___Optional[typing___Text] = None,
        org : typing___Optional[typing___Text] = None,
        user : typing___Optional[typing___Text] = None,
        body : typing___Optional[terraform_sdk___model___cmdb___tf_lock_info_pb2___TFLockInfo] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LockStateRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LockStateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"body",b"body"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"body",b"body",u"org",b"org",u"tfId",b"tfId",u"user",b"user"]) -> None: ...

class LockStateResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___empty_pb2___Empty: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[google___protobuf___empty_pb2___Empty] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> LockStateResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> LockStateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
