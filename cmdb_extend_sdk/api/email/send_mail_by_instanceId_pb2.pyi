# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.empty_pb2 import (
    Empty as google___protobuf___empty_pb2___Empty,
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


class SendMailByInstanceIdRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    send_to_user = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    send_to_group = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    subject = ... # type: typing___Text
    message = ... # type: typing___Text
    cc_to_user = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    cc_to_group = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    send_from_name = ... # type: typing___Text
    contentType = ... # type: typing___Text

    def __init__(self,
        *,
        send_to_user : typing___Optional[typing___Iterable[typing___Text]] = None,
        send_to_group : typing___Optional[typing___Iterable[typing___Text]] = None,
        subject : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        cc_to_user : typing___Optional[typing___Iterable[typing___Text]] = None,
        cc_to_group : typing___Optional[typing___Iterable[typing___Text]] = None,
        send_from_name : typing___Optional[typing___Text] = None,
        contentType : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SendMailByInstanceIdRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SendMailByInstanceIdRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cc_to_group",b"cc_to_group",u"cc_to_user",b"cc_to_user",u"contentType",b"contentType",u"message",b"message",u"send_from_name",b"send_from_name",u"send_to_group",b"send_to_group",u"send_to_user",b"send_to_user",u"subject",b"subject"]) -> None: ...

class SendMailByInstanceIdResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___empty_pb2___Empty: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[google___protobuf___empty_pb2___Empty] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> SendMailByInstanceIdResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> SendMailByInstanceIdResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
