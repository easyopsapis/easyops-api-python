# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from database_delivery_sdk.model.database_delivery.dbinstance_pb2 import (
    DBInstance as database_delivery_sdk___model___database_delivery___dbinstance_pb2___DBInstance,
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


class GetDBServiceRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    dbServiceId = ... # type: typing___Text

    def __init__(self,
        *,
        dbServiceId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetDBServiceRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDBServiceRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dbServiceId",b"dbServiceId"]) -> None: ...

class GetDBServiceResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Owner(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text
        user_email = ... # type: typing___Text
        user_tel = ... # type: typing___Text
        user_type = ... # type: typing___Text
        nickname = ... # type: typing___Text

        def __init__(self,
            *,
            instanceId : typing___Optional[typing___Text] = None,
            user_email : typing___Optional[typing___Text] = None,
            user_tel : typing___Optional[typing___Text] = None,
            user_type : typing___Optional[typing___Text] = None,
            nickname : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetDBServiceResponse.Owner: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDBServiceResponse.Owner: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"nickname",b"nickname",u"user_email",b"user_email",u"user_tel",b"user_tel",u"user_type",b"user_type"]) -> None: ...

    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    dbType = ... # type: typing___Text
    desc = ... # type: typing___Text
    updatedTime = ... # type: builtin___int

    @property
    def dbInstance(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[database_delivery_sdk___model___database_delivery___dbinstance_pb2___DBInstance]: ...

    @property
    def owner(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetDBServiceResponse.Owner]: ...

    def __init__(self,
        *,
        dbInstance : typing___Optional[typing___Iterable[database_delivery_sdk___model___database_delivery___dbinstance_pb2___DBInstance]] = None,
        owner : typing___Optional[typing___Iterable[GetDBServiceResponse.Owner]] = None,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        dbType : typing___Optional[typing___Text] = None,
        desc : typing___Optional[typing___Text] = None,
        updatedTime : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetDBServiceResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDBServiceResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dbInstance",b"dbInstance",u"dbType",b"dbType",u"desc",b"desc",u"instanceId",b"instanceId",u"name",b"name",u"owner",b"owner",u"updatedTime",b"updatedTime"]) -> None: ...

class GetDBServiceResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetDBServiceResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetDBServiceResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetDBServiceResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetDBServiceResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
