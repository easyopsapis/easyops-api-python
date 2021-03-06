# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from cmdb_sdk.model.cmdb.cmdb_object_pb2 import (
    CmdbObject as cmdb_sdk___model___cmdb___cmdb_object_pb2___CmdbObject,
)

from cmdb_sdk.model.cmdb.object_view_pb2 import (
    ObjectView as cmdb_sdk___model___cmdb___object_view_pb2___ObjectView,
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


class CreateRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    name = ... # type: typing___Text
    icon = ... # type: typing___Text
    category = ... # type: typing___Text
    memo = ... # type: typing___Text
    isAbstract = ... # type: builtin___bool
    parentObjectId = ... # type: typing___Text

    @property
    def view(self) -> cmdb_sdk___model___cmdb___object_view_pb2___ObjectView: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        icon : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        view : typing___Optional[cmdb_sdk___model___cmdb___object_view_pb2___ObjectView] = None,
        isAbstract : typing___Optional[builtin___bool] = None,
        parentObjectId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"view",b"view"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"icon",b"icon",u"isAbstract",b"isAbstract",u"memo",b"memo",u"name",b"name",u"objectId",b"objectId",u"parentObjectId",b"parentObjectId",u"view",b"view"]) -> None: ...

class CreateResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> cmdb_sdk___model___cmdb___cmdb_object_pb2___CmdbObject: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[cmdb_sdk___model___cmdb___cmdb_object_pb2___CmdbObject] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
