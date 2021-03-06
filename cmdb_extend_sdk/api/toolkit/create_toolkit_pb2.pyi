# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from cmdb_extend_sdk.model.cmdb_extend.toolkit_pb2 import (
    Toolkit as cmdb_extend_sdk___model___cmdb_extend___toolkit_pb2___Toolkit,
)

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


class CreateToolkitRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text

    @property
    def toolkit(self) -> cmdb_extend_sdk___model___cmdb_extend___toolkit_pb2___Toolkit: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        toolkit : typing___Optional[cmdb_extend_sdk___model___cmdb_extend___toolkit_pb2___Toolkit] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateToolkitRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateToolkitRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"toolkit",b"toolkit"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"objectId",b"objectId",u"toolkit",b"toolkit"]) -> None: ...

class CreateToolkitResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> cmdb_extend_sdk___model___cmdb_extend___toolkit_pb2___Toolkit: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[cmdb_extend_sdk___model___cmdb_extend___toolkit_pb2___Toolkit] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateToolkitResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateToolkitResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
