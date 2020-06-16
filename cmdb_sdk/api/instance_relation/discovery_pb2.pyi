# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from cmdb_sdk.model.cmdb.auto_discovery_instance_pb2 import (
    AutoDiscoveryInstance as cmdb_sdk___model___cmdb___auto_discovery_instance_pb2___AutoDiscoveryInstance,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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


class DiscoveryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Match(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        left_match = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        right_match = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            *,
            left_match : typing___Optional[typing___Iterable[typing___Text]] = None,
            right_match : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DiscoveryRequest.Match: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DiscoveryRequest.Match: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"left_match",b"left_match",u"right_match",b"right_match"]) -> None: ...

    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def left_instance(self) -> google___protobuf___struct_pb2___Struct: ...

        @property
        def right_instance(self) -> google___protobuf___struct_pb2___Struct: ...

        def __init__(self,
            *,
            left_instance : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            right_instance : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DiscoveryRequest.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DiscoveryRequest.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"left_instance",b"left_instance",u"right_instance",b"right_instance"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"left_instance",b"left_instance",u"right_instance",b"right_instance"]) -> None: ...

    relationId = ... # type: typing___Text
    strict = ... # type: builtin___bool

    @property
    def match(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DiscoveryRequest.Match]: ...

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DiscoveryRequest.Data]: ...

    def __init__(self,
        *,
        relationId : typing___Optional[typing___Text] = None,
        match : typing___Optional[typing___Iterable[DiscoveryRequest.Match]] = None,
        data : typing___Optional[typing___Iterable[DiscoveryRequest.Data]] = None,
        strict : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DiscoveryRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DiscoveryRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"match",b"match",u"relationId",b"relationId",u"strict",b"strict"]) -> None: ...

class DiscoveryResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    match_relation_instance_ids = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def left_instance(self) -> cmdb_sdk___model___cmdb___auto_discovery_instance_pb2___AutoDiscoveryInstance: ...

    @property
    def right_instance(self) -> cmdb_sdk___model___cmdb___auto_discovery_instance_pb2___AutoDiscoveryInstance: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        match_relation_instance_ids : typing___Optional[typing___Iterable[typing___Text]] = None,
        left_instance : typing___Optional[cmdb_sdk___model___cmdb___auto_discovery_instance_pb2___AutoDiscoveryInstance] = None,
        right_instance : typing___Optional[cmdb_sdk___model___cmdb___auto_discovery_instance_pb2___AutoDiscoveryInstance] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DiscoveryResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DiscoveryResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"left_instance",b"left_instance",u"right_instance",b"right_instance"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"left_instance",b"left_instance",u"match_relation_instance_ids",b"match_relation_instance_ids",u"right_instance",b"right_instance"]) -> None: ...

class DiscoveryResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DiscoveryResponse]: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[DiscoveryResponse]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DiscoveryResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DiscoveryResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
