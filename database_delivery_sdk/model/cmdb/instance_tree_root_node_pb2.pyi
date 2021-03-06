# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from database_delivery_sdk.model.cmdb.instance_tree_child_node_pb2 import (
    InstanceTreeChildNode as database_delivery_sdk___model___cmdb___instance_tree_child_node_pb2___InstanceTreeChildNode,
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


class InstanceTreeRootNode(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    object_id = ... # type: typing___Text

    @property
    def query(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def fields(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def child(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[database_delivery_sdk___model___cmdb___instance_tree_child_node_pb2___InstanceTreeChildNode]: ...

    def __init__(self,
        *,
        object_id : typing___Optional[typing___Text] = None,
        query : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        fields : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        child : typing___Optional[typing___Iterable[database_delivery_sdk___model___cmdb___instance_tree_child_node_pb2___InstanceTreeChildNode]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> InstanceTreeRootNode: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> InstanceTreeRootNode: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"fields",b"fields",u"query",b"query"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"child",b"child",u"fields",b"fields",u"object_id",b"object_id",u"query",b"query"]) -> None: ...
