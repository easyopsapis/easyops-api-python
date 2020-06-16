# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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


class StrategyPathNodeBasic(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    object_name = ... # type: typing___Text
    relation_id = ... # type: typing___Text
    relation_side_id = ... # type: typing___Text
    relation_side_name = ... # type: typing___Text

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        object_name : typing___Optional[typing___Text] = None,
        relation_id : typing___Optional[typing___Text] = None,
        relation_side_id : typing___Optional[typing___Text] = None,
        relation_side_name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StrategyPathNodeBasic: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StrategyPathNodeBasic: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"objectId",b"objectId",u"object_name",b"object_name",u"relation_id",b"relation_id",u"relation_side_id",b"relation_side_id",u"relation_side_name",b"relation_side_name"]) -> None: ...