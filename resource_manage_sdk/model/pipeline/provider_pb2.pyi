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


class Provider(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Auth(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text
        token = ... # type: typing___Text
        app_id = ... # type: typing___Text
        app_secret = ... # type: typing___Text
        access_private_repos = ... # type: builtin___bool

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            token : typing___Optional[typing___Text] = None,
            app_id : typing___Optional[typing___Text] = None,
            app_secret : typing___Optional[typing___Text] = None,
            access_private_repos : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Provider.Auth: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Provider.Auth: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"access_private_repos",b"access_private_repos",u"app_id",b"app_id",u"app_secret",b"app_secret",u"token",b"token",u"type",b"type"]) -> None: ...

    id = ... # type: typing___Text
    name = ... # type: typing___Text
    type = ... # type: typing___Text
    api_url = ... # type: typing___Text
    default = ... # type: builtin___bool
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    mtime = ... # type: typing___Text

    @property
    def auth(self) -> Provider.Auth: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        api_url : typing___Optional[typing___Text] = None,
        auth : typing___Optional[Provider.Auth] = None,
        default : typing___Optional[builtin___bool] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Provider: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Provider: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"auth",b"auth"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"api_url",b"api_url",u"auth",b"auth",u"creator",b"creator",u"ctime",b"ctime",u"default",b"default",u"id",b"id",u"mtime",b"mtime",u"name",b"name",u"type",b"type"]) -> None: ...
