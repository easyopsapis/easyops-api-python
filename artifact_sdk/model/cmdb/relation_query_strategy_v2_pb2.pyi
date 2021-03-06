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


class RelationQueryStrategyV2(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    byPath = ... # type: typing___Text
    name = ... # type: typing___Text
    type = ... # type: typing___Text
    object_id = ... # type: typing___Text
    ctime = ... # type: typing___Text
    creator = ... # type: typing___Text

    @property
    def path_list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        byPath : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        path_list : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        object_id : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelationQueryStrategyV2: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationQueryStrategyV2: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"byPath",b"byPath",u"creator",b"creator",u"ctime",b"ctime",u"id",b"id",u"name",b"name",u"object_id",b"object_id",u"path_list",b"path_list",u"type",b"type"]) -> None: ...
