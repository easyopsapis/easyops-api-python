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

from micro_app_sdk.model.cmdb_extend.subsystem_dependency_pb2 import (
    SubsystemDependency as micro_app_sdk___model___cmdb_extend___subsystem_dependency_pb2___SubsystemDependency,
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


class SystemDependency(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    abbreviation = ... # type: typing___Text
    name = ... # type: typing___Text
    object_id = ... # type: typing___Text
    instance_id = ... # type: typing___Text

    @property
    def subsystems(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[micro_app_sdk___model___cmdb_extend___subsystem_dependency_pb2___SubsystemDependency]: ...

    def __init__(self,
        *,
        abbreviation : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        object_id : typing___Optional[typing___Text] = None,
        instance_id : typing___Optional[typing___Text] = None,
        subsystems : typing___Optional[typing___Iterable[micro_app_sdk___model___cmdb_extend___subsystem_dependency_pb2___SubsystemDependency]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SystemDependency: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SystemDependency: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"abbreviation",b"abbreviation",u"instance_id",b"instance_id",u"name",b"name",u"object_id",b"object_id",u"subsystems",b"subsystems"]) -> None: ...
