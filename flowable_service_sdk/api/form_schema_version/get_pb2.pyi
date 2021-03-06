# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flowable_service_sdk.model.flowable_service.form_schema_pb2 import (
    FormSchema as flowable_service_sdk___model___flowable_service___form_schema_pb2___FormSchema,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
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


class GetFormSchemaVersionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    formId = ... # type: typing___Text
    versionId = ... # type: typing___Text

    def __init__(self,
        *,
        formId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetFormSchemaVersionRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetFormSchemaVersionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"formId",b"formId",u"versionId",b"versionId"]) -> None: ...

class GetFormSchemaVersionResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    versionName = ... # type: typing___Text
    isMain = ... # type: builtin___bool
    state = ... # type: typing___Text
    memo = ... # type: typing___Text
    creator = ... # type: typing___Text
    formDefinition = ... # type: typing___Text
    ctime = ... # type: typing___Text

    @property
    def formSchema(self) -> flowable_service_sdk___model___flowable_service___form_schema_pb2___FormSchema: ...

    def __init__(self,
        *,
        formSchema : typing___Optional[flowable_service_sdk___model___flowable_service___form_schema_pb2___FormSchema] = None,
        instanceId : typing___Optional[typing___Text] = None,
        versionName : typing___Optional[typing___Text] = None,
        isMain : typing___Optional[builtin___bool] = None,
        state : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        formDefinition : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetFormSchemaVersionResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetFormSchemaVersionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"formSchema",b"formSchema"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"formDefinition",b"formDefinition",u"formSchema",b"formSchema",u"instanceId",b"instanceId",u"isMain",b"isMain",u"memo",b"memo",u"state",b"state",u"versionName",b"versionName"]) -> None: ...

class GetFormSchemaVersionResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetFormSchemaVersionResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetFormSchemaVersionResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetFormSchemaVersionResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetFormSchemaVersionResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
