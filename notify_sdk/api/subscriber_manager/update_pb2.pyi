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

from notify_sdk.model.notify.topic_pb2 import (
    Topic as notify_sdk___model___notify___topic_pb2___Topic,
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


class PubSubscriberUpdateRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    subscriberId = ... # type: typing___Text
    topics = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    name = ... # type: typing___Text
    callback = ... # type: typing___Text
    ensName = ... # type: typing___Text
    retry = ... # type: builtin___int
    topicVersion = ... # type: builtin___int

    def __init__(self,
        *,
        subscriberId : typing___Optional[typing___Text] = None,
        topics : typing___Optional[typing___Iterable[typing___Text]] = None,
        name : typing___Optional[typing___Text] = None,
        callback : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        retry : typing___Optional[builtin___int] = None,
        topicVersion : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PubSubscriberUpdateRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PubSubscriberUpdateRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"callback",b"callback",u"ensName",b"ensName",u"name",b"name",u"retry",b"retry",u"subscriberId",b"subscriberId",u"topicVersion",b"topicVersion",u"topics",b"topics"]) -> None: ...

class PubSubscriberUpdateResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    admin = ... # type: typing___Text
    callback = ... # type: typing___Text
    ensName = ... # type: typing___Text
    retry = ... # type: builtin___int
    mtime = ... # type: typing___Text
    _version = ... # type: builtin___int
    topicVersion = ... # type: builtin___int

    @property
    def topics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[notify_sdk___model___notify___topic_pb2___Topic]: ...

    def __init__(self,
        *,
        topics : typing___Optional[typing___Iterable[notify_sdk___model___notify___topic_pb2___Topic]] = None,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        admin : typing___Optional[typing___Text] = None,
        callback : typing___Optional[typing___Text] = None,
        ensName : typing___Optional[typing___Text] = None,
        retry : typing___Optional[builtin___int] = None,
        mtime : typing___Optional[typing___Text] = None,
        _version : typing___Optional[builtin___int] = None,
        topicVersion : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PubSubscriberUpdateResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PubSubscriberUpdateResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"_version",b"_version",u"admin",b"admin",u"callback",b"callback",u"ensName",b"ensName",u"instanceId",b"instanceId",u"mtime",b"mtime",u"name",b"name",u"retry",b"retry",u"topicVersion",b"topicVersion",u"topics",b"topics"]) -> None: ...

class PubSubscriberUpdateResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> PubSubscriberUpdateResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[PubSubscriberUpdateResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PubSubscriberUpdateResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PubSubscriberUpdateResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
