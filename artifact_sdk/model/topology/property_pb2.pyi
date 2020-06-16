# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from artifact_sdk.model.topology.cmdb_instance_pb2 import (
    CmdbInstance as artifact_sdk___model___topology___cmdb_instance_pb2___CmdbInstance,
)

from artifact_sdk.model.topology.strategy_pb2 import (
    Strategy as artifact_sdk___model___topology___strategy_pb2___Strategy,
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


class Property(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text

    @property
    def strategy(self) -> artifact_sdk___model___topology___strategy_pb2___Strategy: ...

    @property
    def relateInstances(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[artifact_sdk___model___topology___cmdb_instance_pb2___CmdbInstance]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        strategy : typing___Optional[artifact_sdk___model___topology___strategy_pb2___Strategy] = None,
        relateInstances : typing___Optional[typing___Iterable[artifact_sdk___model___topology___cmdb_instance_pb2___CmdbInstance]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Property: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Property: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"strategy",b"strategy"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"objectId",b"objectId",u"relateInstances",b"relateInstances",u"strategy",b"strategy"]) -> None: ...
