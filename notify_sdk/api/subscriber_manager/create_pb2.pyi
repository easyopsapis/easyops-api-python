# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.notify.topic_pb2 import (
    Topic as model___notify___topic_pb2___Topic,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class PubSubscriberCreateRequest(google___protobuf___message___Message):
    topics = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    name = ... # type: typing___Text
    callback = ... # type: typing___Text
    ensName = ... # type: typing___Text
    retry = ... # type: int

    def __init__(self,
        topics : typing___Optional[typing___Iterable[typing___Text]] = None,
        name : typing___Optional[typing___Text] = None,
        callback : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        retry : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PubSubscriberCreateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"callback",u"ensName",u"name",u"retry",u"topics"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"callback",b"ensName",b"name",b"retry",b"topics"]) -> None: ...

class PubSubscriberCreateResponse(google___protobuf___message___Message):
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    org = ... # type: int
    admin = ... # type: typing___Text
    callback = ... # type: typing___Text
    ensName = ... # type: typing___Text
    retry = ... # type: int
    mtime = ... # type: int
    _version = ... # type: int

    @property
    def topics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___notify___topic_pb2___Topic]: ...

    def __init__(self,
        topics : typing___Optional[typing___Iterable[model___notify___topic_pb2___Topic]] = None,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        org : typing___Optional[int] = None,
        admin : typing___Optional[typing___Text] = None,
        callback : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        retry : typing___Optional[int] = None,
        mtime : typing___Optional[int] = None,
        _version : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PubSubscriberCreateResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"_version",u"admin",u"callback",u"ensName",u"instanceId",u"mtime",u"name",u"org",u"retry",u"topics"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"_version",b"admin",b"callback",b"ensName",b"instanceId",b"mtime",b"name",b"org",b"retry",b"topics"]) -> None: ...

class PubSubscriberCreateResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> PubSubscriberCreateResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[PubSubscriberCreateResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PubSubscriberCreateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
