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


class ObjectRelation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name = ... # type: typing___Text
    protected = ... # type: builtin___bool
    relation_id = ... # type: typing___Text
    right_id = ... # type: typing___Text
    right_name = ... # type: typing___Text
    right_description = ... # type: typing___Text
    right_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    right_tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    right_max = ... # type: builtin___int
    right_min = ... # type: builtin___int
    right_object_id = ... # type: typing___Text
    left_id = ... # type: typing___Text
    left_name = ... # type: typing___Text
    left_description = ... # type: typing___Text
    left_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    left_tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    left_max = ... # type: builtin___int
    left_min = ... # type: builtin___int
    left_object_id = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    _ts = ... # type: builtin___int
    _version = ... # type: builtin___int
    isInherit = ... # type: builtin___bool

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        protected : typing___Optional[builtin___bool] = None,
        relation_id : typing___Optional[typing___Text] = None,
        right_id : typing___Optional[typing___Text] = None,
        right_name : typing___Optional[typing___Text] = None,
        right_description : typing___Optional[typing___Text] = None,
        right_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
        right_tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        right_max : typing___Optional[builtin___int] = None,
        right_min : typing___Optional[builtin___int] = None,
        right_object_id : typing___Optional[typing___Text] = None,
        left_id : typing___Optional[typing___Text] = None,
        left_name : typing___Optional[typing___Text] = None,
        left_description : typing___Optional[typing___Text] = None,
        left_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
        left_tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        left_max : typing___Optional[builtin___int] = None,
        left_min : typing___Optional[builtin___int] = None,
        left_object_id : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        _ts : typing___Optional[builtin___int] = None,
        _version : typing___Optional[builtin___int] = None,
        isInherit : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ObjectRelation: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ObjectRelation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"_ts",b"_ts",u"_version",b"_version",u"creator",b"creator",u"ctime",b"ctime",u"isInherit",b"isInherit",u"left_description",b"left_description",u"left_groups",b"left_groups",u"left_id",b"left_id",u"left_max",b"left_max",u"left_min",b"left_min",u"left_name",b"left_name",u"left_object_id",b"left_object_id",u"left_tags",b"left_tags",u"name",b"name",u"protected",b"protected",u"relation_id",b"relation_id",u"right_description",b"right_description",u"right_groups",b"right_groups",u"right_id",b"right_id",u"right_max",b"right_max",u"right_min",b"right_min",u"right_name",b"right_name",u"right_object_id",b"right_object_id",u"right_tags",b"right_tags"]) -> None: ...
