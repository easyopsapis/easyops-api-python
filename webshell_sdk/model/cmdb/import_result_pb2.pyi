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

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    Union as typing___Union,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)

from webshell_sdk.model.cmdb.import_status_pb2 import (
    ImportStatus as webshell_sdk___model___cmdb___import_status_pb2___ImportStatus,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class ImportResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class IndexListResult(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        code = ... # type: builtin___int
        message = ... # type: typing___Text
        name = ... # type: typing___Text
        propertyIds = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        unique = ... # type: builtin___bool

        def __init__(self,
            *,
            code : typing___Optional[builtin___int] = None,
            message : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            propertyIds : typing___Optional[typing___Iterable[typing___Text]] = None,
            unique : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ImportResult.IndexListResult: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportResult.IndexListResult: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"message",b"message",u"name",b"name",u"propertyIds",b"propertyIds",u"unique",b"unique"]) -> None: ...

    objectId = ... # type: typing___Text
    name = ... # type: typing___Text
    category = ... # type: typing___Text
    memo = ... # type: typing___Text
    protected = ... # type: builtin___bool
    system = ... # type: typing___Text
    code = ... # type: builtin___int
    message = ... # type: typing___Text
    is_create = ... # type: builtin___bool

    @property
    def info_result(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]: ...

    @property
    def relation_group_result(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]: ...

    @property
    def attr_list_result(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]: ...

    @property
    def relation_list_result(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]: ...

    @property
    def index_list_result(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ImportResult.IndexListResult]: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        protected : typing___Optional[builtin___bool] = None,
        system : typing___Optional[typing___Text] = None,
        code : typing___Optional[builtin___int] = None,
        message : typing___Optional[typing___Text] = None,
        info_result : typing___Optional[typing___Iterable[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]] = None,
        relation_group_result : typing___Optional[typing___Iterable[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]] = None,
        attr_list_result : typing___Optional[typing___Iterable[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]] = None,
        relation_list_result : typing___Optional[typing___Iterable[webshell_sdk___model___cmdb___import_status_pb2___ImportStatus]] = None,
        index_list_result : typing___Optional[typing___Iterable[ImportResult.IndexListResult]] = None,
        is_create : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ImportResult: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"attr_list_result",b"attr_list_result",u"category",b"category",u"code",b"code",u"index_list_result",b"index_list_result",u"info_result",b"info_result",u"is_create",b"is_create",u"memo",b"memo",u"message",b"message",u"name",b"name",u"objectId",b"objectId",u"protected",b"protected",u"relation_group_result",b"relation_group_result",u"relation_list_result",b"relation_list_result",u"system",b"system"]) -> None: ...
