# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from cmdb_sdk.model.cmdb.object_import_pb2 import (
    ObjectImport as cmdb_sdk___model___cmdb___object_import_pb2___ObjectImport,
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


class ImportObjectRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def body(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[cmdb_sdk___model___cmdb___object_import_pb2___ObjectImport]: ...

    def __init__(self,
        *,
        body : typing___Optional[typing___Iterable[cmdb_sdk___model___cmdb___object_import_pb2___ObjectImport]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ImportObjectRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportObjectRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"body",b"body"]) -> None: ...

class ImportObjectResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class AttrList(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            id = ... # type: typing___Text
            name = ... # type: typing___Text
            code = ... # type: builtin___int
            error = ... # type: typing___Text

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                code : typing___Optional[builtin___int] = None,
                error : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ImportObjectResponse.Data.AttrList: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportObjectResponse.Data.AttrList: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"error",b"error",u"id",b"id",u"name",b"name"]) -> None: ...

        class RelationList(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            relation_id = ... # type: typing___Text
            left_description = ... # type: typing___Text
            right_description = ... # type: typing___Text
            left_name = ... # type: typing___Text
            right_name = ... # type: typing___Text
            code = ... # type: builtin___int
            error = ... # type: typing___Text

            def __init__(self,
                *,
                relation_id : typing___Optional[typing___Text] = None,
                left_description : typing___Optional[typing___Text] = None,
                right_description : typing___Optional[typing___Text] = None,
                left_name : typing___Optional[typing___Text] = None,
                right_name : typing___Optional[typing___Text] = None,
                code : typing___Optional[builtin___int] = None,
                error : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ImportObjectResponse.Data.RelationList: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportObjectResponse.Data.RelationList: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"error",b"error",u"left_description",b"left_description",u"left_name",b"left_name",u"relation_id",b"relation_id",u"right_description",b"right_description",u"right_name",b"right_name"]) -> None: ...

        objectId = ... # type: typing___Text
        name = ... # type: typing___Text
        code = ... # type: builtin___int
        error = ... # type: typing___Text

        @property
        def attrList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ImportObjectResponse.Data.AttrList]: ...

        @property
        def relation_list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ImportObjectResponse.Data.RelationList]: ...

        def __init__(self,
            *,
            objectId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            code : typing___Optional[builtin___int] = None,
            error : typing___Optional[typing___Text] = None,
            attrList : typing___Optional[typing___Iterable[ImportObjectResponse.Data.AttrList]] = None,
            relation_list : typing___Optional[typing___Iterable[ImportObjectResponse.Data.RelationList]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ImportObjectResponse.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportObjectResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"attrList",b"attrList",u"code",b"code",u"error",b"error",u"name",b"name",u"objectId",b"objectId",u"relation_list",b"relation_list"]) -> None: ...

    code = ... # type: builtin___int
    error = ... # type: typing___Text
    message = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ImportObjectResponse.Data]: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        error : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[ImportObjectResponse.Data]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ImportObjectResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportObjectResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"data",b"data",u"error",b"error",u"message",b"message"]) -> None: ...

class ImportObjectResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ImportObjectResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ImportObjectResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ImportObjectResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ImportObjectResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...