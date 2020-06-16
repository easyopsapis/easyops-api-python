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


class UpdateCollectionConfigRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Kwargs(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> google___protobuf___struct_pb2___Value: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigRequest.Kwargs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigRequest.Kwargs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class Env(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text

        @property
        def value(self) -> google___protobuf___struct_pb2___Value: ...

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigRequest.Env: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigRequest.Env: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"value",b"value"]) -> None: ...

    class Script(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        version = ... # type: typing___Text
        type = ... # type: typing___Text
        content = ... # type: typing___Text
        name = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            version : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            content : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigRequest.Script: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigRequest.Script: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content",b"content",u"id",b"id",u"name",b"name",u"type",b"type",u"version",b"version"]) -> None: ...

    class HostRange(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Query(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            key = ... # type: typing___Text
            op = ... # type: typing___Text

            @property
            def value(self) -> google___protobuf___struct_pb2___Value: ...

            def __init__(self,
                *,
                key : typing___Optional[typing___Text] = None,
                op : typing___Optional[typing___Text] = None,
                value : typing___Optional[google___protobuf___struct_pb2___Value] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigRequest.HostRange.Query: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigRequest.HostRange.Query: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"op",b"op",u"value",b"value"]) -> None: ...

        objectId = ... # type: typing___Text
        hostKey = ... # type: typing___Text
        querier = ... # type: typing___Text
        type = ... # type: typing___Text
        queryString = ... # type: typing___Text
        queryId = ... # type: typing___Text

        @property
        def query(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[UpdateCollectionConfigRequest.HostRange.Query]: ...

        def __init__(self,
            *,
            objectId : typing___Optional[typing___Text] = None,
            hostKey : typing___Optional[typing___Text] = None,
            querier : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            queryString : typing___Optional[typing___Text] = None,
            queryId : typing___Optional[typing___Text] = None,
            query : typing___Optional[typing___Iterable[UpdateCollectionConfigRequest.HostRange.Query]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigRequest.HostRange: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigRequest.HostRange: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"hostKey",b"hostKey",u"objectId",b"objectId",u"querier",b"querier",u"query",b"query",u"queryId",b"queryId",u"queryString",b"queryString",u"type",b"type"]) -> None: ...

    id = ... # type: typing___Text
    name = ... # type: typing___Text
    timeout = ... # type: builtin___int
    disabled = ... # type: builtin___bool
    labels = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    ignoreInvalid = ... # type: builtin___bool
    interval = ... # type: builtin___int
    cacheTtl = ... # type: builtin___int
    timeRange = ... # type: typing___Text
    clazzId = ... # type: typing___Text
    objectId = ... # type: typing___Text
    instanceIdMacro = ... # type: typing___Text

    @property
    def kwargs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[UpdateCollectionConfigRequest.Kwargs]: ...

    @property
    def env(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[UpdateCollectionConfigRequest.Env]: ...

    @property
    def script(self) -> UpdateCollectionConfigRequest.Script: ...

    @property
    def hostRange(self) -> UpdateCollectionConfigRequest.HostRange: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        kwargs : typing___Optional[typing___Iterable[UpdateCollectionConfigRequest.Kwargs]] = None,
        timeout : typing___Optional[builtin___int] = None,
        env : typing___Optional[typing___Iterable[UpdateCollectionConfigRequest.Env]] = None,
        disabled : typing___Optional[builtin___bool] = None,
        labels : typing___Optional[typing___Iterable[typing___Text]] = None,
        script : typing___Optional[UpdateCollectionConfigRequest.Script] = None,
        ignoreInvalid : typing___Optional[builtin___bool] = None,
        hostRange : typing___Optional[UpdateCollectionConfigRequest.HostRange] = None,
        interval : typing___Optional[builtin___int] = None,
        cacheTtl : typing___Optional[builtin___int] = None,
        timeRange : typing___Optional[typing___Text] = None,
        clazzId : typing___Optional[typing___Text] = None,
        objectId : typing___Optional[typing___Text] = None,
        instanceIdMacro : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"hostRange",b"hostRange",u"script",b"script"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cacheTtl",b"cacheTtl",u"clazzId",b"clazzId",u"disabled",b"disabled",u"env",b"env",u"hostRange",b"hostRange",u"id",b"id",u"ignoreInvalid",b"ignoreInvalid",u"instanceIdMacro",b"instanceIdMacro",u"interval",b"interval",u"kwargs",b"kwargs",u"labels",b"labels",u"name",b"name",u"objectId",b"objectId",u"script",b"script",u"timeRange",b"timeRange",u"timeout",b"timeout"]) -> None: ...

class UpdateCollectionConfigResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id"]) -> None: ...

class UpdateCollectionConfigResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> UpdateCollectionConfigResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[UpdateCollectionConfigResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> UpdateCollectionConfigResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> UpdateCollectionConfigResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
