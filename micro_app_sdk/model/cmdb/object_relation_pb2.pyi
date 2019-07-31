# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ObjectRelation(google___protobuf___message___Message):
    name = ... # type: typing___Text
    protected = ... # type: bool
    relation_id = ... # type: typing___Text
    right_id = ... # type: typing___Text
    right_name = ... # type: typing___Text
    right_description = ... # type: typing___Text
    right_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    right_tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    right_max = ... # type: int
    right_min = ... # type: int
    right_object_id = ... # type: typing___Text
    left_id = ... # type: typing___Text
    left_name = ... # type: typing___Text
    left_description = ... # type: typing___Text
    left_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    left_tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    left_max = ... # type: int
    left_min = ... # type: int
    left_object_id = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    _ts = ... # type: int
    _version = ... # type: int

    def __init__(self,
        name : typing___Optional[typing___Text] = None,
        protected : typing___Optional[bool] = None,
        relation_id : typing___Optional[typing___Text] = None,
        right_id : typing___Optional[typing___Text] = None,
        right_name : typing___Optional[typing___Text] = None,
        right_description : typing___Optional[typing___Text] = None,
        right_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
        right_tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        right_max : typing___Optional[int] = None,
        right_min : typing___Optional[int] = None,
        right_object_id : typing___Optional[typing___Text] = None,
        left_id : typing___Optional[typing___Text] = None,
        left_name : typing___Optional[typing___Text] = None,
        left_description : typing___Optional[typing___Text] = None,
        left_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
        left_tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        left_max : typing___Optional[int] = None,
        left_min : typing___Optional[int] = None,
        left_object_id : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        _ts : typing___Optional[int] = None,
        _version : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ObjectRelation: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"_ts",u"_version",u"creator",u"ctime",u"left_description",u"left_groups",u"left_id",u"left_max",u"left_min",u"left_name",u"left_object_id",u"left_tags",u"name",u"protected",u"relation_id",u"right_description",u"right_groups",u"right_id",u"right_max",u"right_min",u"right_name",u"right_object_id",u"right_tags"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"_ts",b"_version",b"creator",b"ctime",b"left_description",b"left_groups",b"left_id",b"left_max",b"left_min",b"left_name",b"left_object_id",b"left_tags",b"name",b"protected",b"relation_id",b"right_description",b"right_groups",b"right_id",b"right_max",b"right_min",b"right_name",b"right_object_id",b"right_tags"]) -> None: ...
