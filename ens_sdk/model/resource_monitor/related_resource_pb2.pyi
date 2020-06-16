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


class RelatedResource(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class RelatedInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        label = ... # type: typing___Text
        reverseQueryKey = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            label : typing___Optional[typing___Text] = None,
            reverseQueryKey : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> RelatedResource.RelatedInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelatedResource.RelatedInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"label",b"label",u"reverseQueryKey",b"reverseQueryKey"]) -> None: ...

    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    objectId = ... # type: typing___Text
    relatedObjectId = ... # type: typing___Text
    query = ... # type: typing___Text

    @property
    def relatedInfo(self) -> RelatedResource.RelatedInfo: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        objectId : typing___Optional[typing___Text] = None,
        relatedObjectId : typing___Optional[typing___Text] = None,
        query : typing___Optional[typing___Text] = None,
        relatedInfo : typing___Optional[RelatedResource.RelatedInfo] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> RelatedResource: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> RelatedResource: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"relatedInfo",b"relatedInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"name",b"name",u"objectId",b"objectId",u"query",b"query",u"relatedInfo",b"relatedInfo",u"relatedObjectId",b"relatedObjectId"]) -> None: ...