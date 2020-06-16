# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from anxin_service_sdk.model.cmdb_extend.app_dependency_pb2 import (
    AppDependency as anxin_service_sdk___model___cmdb_extend___app_dependency_pb2___AppDependency,
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


class SubsystemDependency(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ConnectSubsystems(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        abbreviation = ... # type: typing___Text
        object_id = ... # type: typing___Text
        instance_id = ... # type: typing___Text
        name = ... # type: typing___Text

        def __init__(self,
            *,
            abbreviation : typing___Optional[typing___Text] = None,
            object_id : typing___Optional[typing___Text] = None,
            instance_id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> SubsystemDependency.ConnectSubsystems: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SubsystemDependency.ConnectSubsystems: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"abbreviation",b"abbreviation",u"instance_id",b"instance_id",u"name",b"name",u"object_id",b"object_id"]) -> None: ...

    abbreviation = ... # type: typing___Text
    name = ... # type: typing___Text
    object_id = ... # type: typing___Text
    instance_id = ... # type: typing___Text

    @property
    def components(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[anxin_service_sdk___model___cmdb_extend___app_dependency_pb2___AppDependency]: ...

    @property
    def connect_subsystems(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[SubsystemDependency.ConnectSubsystems]: ...

    def __init__(self,
        *,
        abbreviation : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        object_id : typing___Optional[typing___Text] = None,
        instance_id : typing___Optional[typing___Text] = None,
        components : typing___Optional[typing___Iterable[anxin_service_sdk___model___cmdb_extend___app_dependency_pb2___AppDependency]] = None,
        connect_subsystems : typing___Optional[typing___Iterable[SubsystemDependency.ConnectSubsystems]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SubsystemDependency: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SubsystemDependency: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"abbreviation",b"abbreviation",u"components",b"components",u"connect_subsystems",b"connect_subsystems",u"instance_id",b"instance_id",u"name",b"name",u"object_id",b"object_id"]) -> None: ...
