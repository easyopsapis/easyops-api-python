# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from flowable_service_sdk.model.flowable_service.form_schema_version_pb2 import (
    FormSchemaVersion as flowable_service_sdk___model___flowable_service___form_schema_version_pb2___FormSchemaVersion,
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


class SaveFormSchemaRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    state = ... # type: typing___Text
    vMemo = ... # type: typing___Text
    name = ... # type: typing___Text
    category = ... # type: typing___Text
    memo = ... # type: typing___Text
    formDefinition = ... # type: typing___Text
    versionName = ... # type: typing___Text

    def __init__(self,
        *,
        state : typing___Optional[typing___Text] = None,
        vMemo : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        formDefinition : typing___Optional[typing___Text] = None,
        versionName : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SaveFormSchemaRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SaveFormSchemaRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"formDefinition",b"formDefinition",u"memo",b"memo",u"name",b"name",u"state",b"state",u"vMemo",b"vMemo",u"versionName",b"versionName"]) -> None: ...

class SaveFormSchemaResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    category = ... # type: typing___Text
    memo = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text

    @property
    def lastestVersion(self) -> flowable_service_sdk___model___flowable_service___form_schema_version_pb2___FormSchemaVersion: ...

    def __init__(self,
        *,
        lastestVersion : typing___Optional[flowable_service_sdk___model___flowable_service___form_schema_version_pb2___FormSchemaVersion] = None,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SaveFormSchemaResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SaveFormSchemaResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"lastestVersion",b"lastestVersion"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"category",b"category",u"creator",b"creator",u"ctime",b"ctime",u"instanceId",b"instanceId",u"lastestVersion",b"lastestVersion",u"memo",b"memo",u"name",b"name"]) -> None: ...

class SaveFormSchemaResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> SaveFormSchemaResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[SaveFormSchemaResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SaveFormSchemaResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SaveFormSchemaResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
