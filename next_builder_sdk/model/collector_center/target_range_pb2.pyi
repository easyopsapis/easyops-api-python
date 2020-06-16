# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from next_builder_sdk.model.collector_center.cmdb_host_search_pb2 import (
    CmdbHostSearch as next_builder_sdk___model___collector_center___cmdb_host_search_pb2___CmdbHostSearch,
)

from next_builder_sdk.model.collector_center.cmdb_host_strategy_pb2 import (
    CmdbHostStrategy as next_builder_sdk___model___collector_center___cmdb_host_strategy_pb2___CmdbHostStrategy,
)

from next_builder_sdk.model.collector_center.cmdb_relation_search_pb2 import (
    CmdbRelationSearch as next_builder_sdk___model___collector_center___cmdb_relation_search_pb2___CmdbRelationSearch,
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


class TargetRange(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: typing___Text

    @property
    def cmdbRelationSearch(self) -> next_builder_sdk___model___collector_center___cmdb_relation_search_pb2___CmdbRelationSearch: ...

    @property
    def cmdbHostSearch(self) -> next_builder_sdk___model___collector_center___cmdb_host_search_pb2___CmdbHostSearch: ...

    @property
    def cmdbHostStrategy(self) -> next_builder_sdk___model___collector_center___cmdb_host_strategy_pb2___CmdbHostStrategy: ...

    def __init__(self,
        *,
        type : typing___Optional[typing___Text] = None,
        cmdbRelationSearch : typing___Optional[next_builder_sdk___model___collector_center___cmdb_relation_search_pb2___CmdbRelationSearch] = None,
        cmdbHostSearch : typing___Optional[next_builder_sdk___model___collector_center___cmdb_host_search_pb2___CmdbHostSearch] = None,
        cmdbHostStrategy : typing___Optional[next_builder_sdk___model___collector_center___cmdb_host_strategy_pb2___CmdbHostStrategy] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TargetRange: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TargetRange: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"cmdbHostSearch",b"cmdbHostSearch",u"cmdbHostStrategy",b"cmdbHostStrategy",u"cmdbRelationSearch",b"cmdbRelationSearch"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cmdbHostSearch",b"cmdbHostSearch",u"cmdbHostStrategy",b"cmdbHostStrategy",u"cmdbRelationSearch",b"cmdbRelationSearch",u"type",b"type"]) -> None: ...
