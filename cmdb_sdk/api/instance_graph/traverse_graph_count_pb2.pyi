# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from cmdb_sdk.model.cmdb.traverse_child_node_pb2 import (
    TraverseChildNode as cmdb_sdk___model___cmdb___traverse_child_node_pb2___TraverseChildNode,
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

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
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


class TraverseGraphCountRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    object_id = ... # type: typing___Text

    @property
    def query(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def fields(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def child(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cmdb_sdk___model___cmdb___traverse_child_node_pb2___TraverseChildNode]: ...

    def __init__(self,
        *,
        object_id : typing___Optional[typing___Text] = None,
        query : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        fields : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        child : typing___Optional[typing___Iterable[cmdb_sdk___model___cmdb___traverse_child_node_pb2___TraverseChildNode]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TraverseGraphCountRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TraverseGraphCountRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"fields",b"fields",u"query",b"query"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"child",b"child",u"fields",b"fields",u"object_id",b"object_id",u"query",b"query"]) -> None: ...

class TraverseGraphCountResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        object_id = ... # type: typing___Text
        path = ... # type: typing___Text
        count = ... # type: builtin___int

        def __init__(self,
            *,
            object_id : typing___Optional[typing___Text] = None,
            path : typing___Optional[typing___Text] = None,
            count : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> TraverseGraphCountResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TraverseGraphCountResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"count",b"count",u"object_id",b"object_id",u"path",b"path"]) -> None: ...

    object_id = ... # type: typing___Text
    instanceId = ... # type: typing___Text

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TraverseGraphCountResponse.List]: ...

    def __init__(self,
        *,
        object_id : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        list : typing___Optional[typing___Iterable[TraverseGraphCountResponse.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TraverseGraphCountResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TraverseGraphCountResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"list",b"list",u"object_id",b"object_id"]) -> None: ...

class TraverseGraphCountResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TraverseGraphCountResponse]: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[TraverseGraphCountResponse]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TraverseGraphCountResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TraverseGraphCountResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
