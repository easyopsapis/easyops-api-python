# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from collector_center_sdk.model.topology.nodeStyle_pb2 import (
    NodeStyle as collector_center_sdk___model___topology___nodeStyle_pb2___NodeStyle,
)

from collector_center_sdk.model.topology.property_pb2 import (
    Property as collector_center_sdk___model___topology___property_pb2___Property,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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


class Node(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    label = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    dataSource = ... # type: typing___Text
    relateNodes = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    id = ... # type: typing___Text
    collapse = ... # type: builtin___bool

    @property
    def property(self) -> collector_center_sdk___model___topology___property_pb2___Property: ...

    @property
    def style(self) -> collector_center_sdk___model___topology___nodeStyle_pb2___NodeStyle: ...

    def __init__(self,
        *,
        label : typing___Optional[typing___Iterable[typing___Text]] = None,
        dataSource : typing___Optional[typing___Text] = None,
        relateNodes : typing___Optional[typing___Iterable[typing___Text]] = None,
        id : typing___Optional[typing___Text] = None,
        property : typing___Optional[collector_center_sdk___model___topology___property_pb2___Property] = None,
        collapse : typing___Optional[builtin___bool] = None,
        style : typing___Optional[collector_center_sdk___model___topology___nodeStyle_pb2___NodeStyle] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Node: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Node: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"property",b"property",u"style",b"style"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"collapse",b"collapse",u"dataSource",b"dataSource",u"id",b"id",u"label",b"label",u"property",b"property",u"relateNodes",b"relateNodes",u"style",b"style"]) -> None: ...
