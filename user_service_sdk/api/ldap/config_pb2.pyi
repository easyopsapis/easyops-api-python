# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.empty_pb2 import (
    Empty as google___protobuf___empty_pb2___Empty,
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


class ConfigRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Conf(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        user_search_dn = ... # type: typing___Text
        user_filter = ... # type: typing___Text
        manager_dn = ... # type: typing___Text
        manager_password = ... # type: typing___Text
        username = ... # type: typing___Text
        org = ... # type: builtin___int

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            user_search_dn : typing___Optional[typing___Text] = None,
            user_filter : typing___Optional[typing___Text] = None,
            manager_dn : typing___Optional[typing___Text] = None,
            manager_password : typing___Optional[typing___Text] = None,
            username : typing___Optional[typing___Text] = None,
            org : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ConfigRequest.Conf: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ConfigRequest.Conf: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"manager_dn",b"manager_dn",u"manager_password",b"manager_password",u"name",b"name",u"org",b"org",u"user_filter",b"user_filter",u"user_search_dn",b"user_search_dn",u"username",b"username"]) -> None: ...

    key = ... # type: typing___Text

    @property
    def conf(self) -> ConfigRequest.Conf: ...

    def __init__(self,
        *,
        key : typing___Optional[typing___Text] = None,
        conf : typing___Optional[ConfigRequest.Conf] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ConfigRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ConfigRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"conf",b"conf"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"conf",b"conf",u"key",b"key"]) -> None: ...

class ConfigResponseWrapper(google___protobuf___message___Message):
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
        def FromString(cls, s: builtin___bytes) -> ConfigResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ConfigResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...