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


class AutoDiscoveryRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Body(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        upsert = ... # type: builtin___bool

        @property
        def filter(self) -> google___protobuf___struct_pb2___Struct: ...

        @property
        def update(self) -> google___protobuf___struct_pb2___Struct: ...

        def __init__(self,
            *,
            filter : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            update : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            upsert : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AutoDiscoveryRequest.Body: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AutoDiscoveryRequest.Body: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"filter",b"filter",u"update",b"update"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"filter",b"filter",u"update",b"update",u"upsert",b"upsert"]) -> None: ...

    objectId = ... # type: typing___Text

    @property
    def body(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AutoDiscoveryRequest.Body]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        body : typing___Optional[typing___Iterable[AutoDiscoveryRequest.Body]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AutoDiscoveryRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AutoDiscoveryRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"body",b"body",u"objectId",b"objectId"]) -> None: ...

class AutoDiscoveryResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text
        code = ... # type: builtin___int
        matched = ... # type: builtin___bool
        effected = ... # type: builtin___bool
        message = ... # type: typing___Text

        def __init__(self,
            *,
            instanceId : typing___Optional[typing___Text] = None,
            code : typing___Optional[builtin___int] = None,
            matched : typing___Optional[builtin___bool] = None,
            effected : typing___Optional[builtin___bool] = None,
            message : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AutoDiscoveryResponse.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AutoDiscoveryResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"effected",b"effected",u"instanceId",b"instanceId",u"matched",b"matched",u"message",b"message"]) -> None: ...

    code = ... # type: builtin___int
    error = ... # type: typing___Text
    message = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AutoDiscoveryResponse.Data]: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        error : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[AutoDiscoveryResponse.Data]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AutoDiscoveryResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AutoDiscoveryResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data",b"data",u"error",b"error",u"message",b"message"]) -> None: ...

class AutoDiscoveryResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> AutoDiscoveryResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[AutoDiscoveryResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AutoDiscoveryResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AutoDiscoveryResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
