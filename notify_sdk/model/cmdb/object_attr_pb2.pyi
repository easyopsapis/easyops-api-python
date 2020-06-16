# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from notify_sdk.model.cmdb.object_attr_value_pb2 import (
    ObjectAttrValue as notify_sdk___model___cmdb___object_attr_value_pb2___ObjectAttrValue,
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


class ObjectAttr(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    protected = ... # type: builtin___bool
    custom = ... # type: typing___Text
    readonly = ... # type: typing___Text
    required = ... # type: typing___Text
    unique = ... # type: typing___Text
    tag = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    wordIndexDenied = ... # type: builtin___bool
    description = ... # type: typing___Text
    tips = ... # type: typing___Text
    isInherit = ... # type: builtin___bool

    @property
    def value(self) -> notify_sdk___model___cmdb___object_attr_value_pb2___ObjectAttrValue: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        protected : typing___Optional[builtin___bool] = None,
        custom : typing___Optional[typing___Text] = None,
        readonly : typing___Optional[typing___Text] = None,
        required : typing___Optional[typing___Text] = None,
        unique : typing___Optional[typing___Text] = None,
        tag : typing___Optional[typing___Iterable[typing___Text]] = None,
        value : typing___Optional[notify_sdk___model___cmdb___object_attr_value_pb2___ObjectAttrValue] = None,
        wordIndexDenied : typing___Optional[builtin___bool] = None,
        description : typing___Optional[typing___Text] = None,
        tips : typing___Optional[typing___Text] = None,
        isInherit : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ObjectAttr: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectAttr: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"custom",b"custom",u"description",b"description",u"id",b"id",u"isInherit",b"isInherit",u"name",b"name",u"protected",b"protected",u"readonly",b"readonly",u"required",b"required",u"tag",b"tag",u"tips",b"tips",u"unique",b"unique",u"value",b"value",u"wordIndexDenied",b"wordIndexDenied"]) -> None: ...
