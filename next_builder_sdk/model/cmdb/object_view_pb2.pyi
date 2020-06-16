# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
    Value as google___protobuf___struct_pb2___Value,
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


class ObjectView(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    visible = ... # type: builtin___bool
    showHideAttrs = ... # type: builtin___bool
    hide_columns = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    attr_order = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    show_key = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def relation_view(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def attr_authorizers(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        visible : typing___Optional[builtin___bool] = None,
        showHideAttrs : typing___Optional[builtin___bool] = None,
        hide_columns : typing___Optional[typing___Iterable[typing___Text]] = None,
        relation_view : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        attr_order : typing___Optional[typing___Iterable[typing___Text]] = None,
        show_key : typing___Optional[typing___Iterable[typing___Text]] = None,
        attr_authorizers : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ObjectView: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectView: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"attr_authorizers",b"attr_authorizers",u"relation_view",b"relation_view"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"attr_authorizers",b"attr_authorizers",u"attr_order",b"attr_order",u"hide_columns",b"hide_columns",u"relation_view",b"relation_view",u"showHideAttrs",b"showHideAttrs",u"show_key",b"show_key",u"visible",b"visible"]) -> None: ...