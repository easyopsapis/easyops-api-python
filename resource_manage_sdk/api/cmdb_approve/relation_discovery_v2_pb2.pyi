# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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

from resource_manage_sdk.model.cmdb.instance_relation_pair_pb2 import (
    InstanceRelationPair as resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair,
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


class RelationDiscoveryV2Request(google___protobuf___message___Message):
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
            def FromString(cls, s: builtin___bytes) -> RelationDiscoveryV2Request.Match: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationDiscoveryV2Request.Match: ...
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
            def FromString(cls, s: builtin___bytes) -> RelationDiscoveryV2Request.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationDiscoveryV2Request.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"left_instance",b"left_instance",u"right_instance",b"right_instance"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"left_instance",b"left_instance",u"right_instance",b"right_instance"]) -> None: ...

    relationId = ... # type: typing___Text
    strict = ... # type: builtin___bool
    operation = ... # type: typing___Text
    source = ... # type: typing___Text
    mainSideId = ... # type: typing___Text

    @property
    def match(self) -> RelationDiscoveryV2Request.Match: ...

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RelationDiscoveryV2Request.Data]: ...

    def __init__(self,
        *,
        relationId : typing___Optional[typing___Text] = None,
        match : typing___Optional[RelationDiscoveryV2Request.Match] = None,
        data : typing___Optional[typing___Iterable[RelationDiscoveryV2Request.Data]] = None,
        strict : typing___Optional[builtin___bool] = None,
        operation : typing___Optional[typing___Text] = None,
        source : typing___Optional[typing___Text] = None,
        mainSideId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelationDiscoveryV2Request: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationDiscoveryV2Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"match",b"match"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"mainSideId",b"mainSideId",u"match",b"match",u"operation",b"operation",u"relationId",b"relationId",u"source",b"source",u"strict",b"strict"]) -> None: ...

class RelationDiscoveryV2Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        code = ... # type: builtin___int
        message = ... # type: typing___Text
        left_object_id = ... # type: typing___Text
        right_object_id = ... # type: typing___Text

        @property
        def connect_success(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]: ...

        @property
        def connect_fail(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]: ...

        @property
        def disconnect_success(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]: ...

        @property
        def disconnect_fail(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]: ...

        @property
        def approve_list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]: ...

        def __init__(self,
            *,
            code : typing___Optional[builtin___int] = None,
            message : typing___Optional[typing___Text] = None,
            left_object_id : typing___Optional[typing___Text] = None,
            right_object_id : typing___Optional[typing___Text] = None,
            connect_success : typing___Optional[typing___Iterable[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]] = None,
            connect_fail : typing___Optional[typing___Iterable[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]] = None,
            disconnect_success : typing___Optional[typing___Iterable[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]] = None,
            disconnect_fail : typing___Optional[typing___Iterable[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]] = None,
            approve_list : typing___Optional[typing___Iterable[resource_manage_sdk___model___cmdb___instance_relation_pair_pb2___InstanceRelationPair]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> RelationDiscoveryV2Response.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationDiscoveryV2Response.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"approve_list",b"approve_list",u"code",b"code",u"connect_fail",b"connect_fail",u"connect_success",b"connect_success",u"disconnect_fail",b"disconnect_fail",u"disconnect_success",b"disconnect_success",u"left_object_id",b"left_object_id",u"message",b"message",u"right_object_id",b"right_object_id"]) -> None: ...

    code = ... # type: builtin___int
    error = ... # type: typing___Text
    message = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[RelationDiscoveryV2Response.Data]: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        error : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[RelationDiscoveryV2Response.Data]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelationDiscoveryV2Response: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationDiscoveryV2Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data",b"data",u"error",b"error",u"message",b"message"]) -> None: ...

class RelationDiscoveryV2ResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> RelationDiscoveryV2Response: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[RelationDiscoveryV2Response] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelationDiscoveryV2ResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelationDiscoveryV2ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
