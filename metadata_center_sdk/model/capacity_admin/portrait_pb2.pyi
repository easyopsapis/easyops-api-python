# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from metadata_center_sdk.model.capacity_admin.portrait_config_pb2 import (
    PortraitConfig as metadata_center_sdk___model___capacity_admin___portrait_config_pb2___PortraitConfig,
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


class Portrait(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    charset = ... # type: typing___Text
    user = ... # type: typing___Text
    memo = ... # type: typing___Text
    ctime = ... # type: typing___Text
    creator = ... # type: typing___Text

    @property
    def config(self) -> metadata_center_sdk___model___capacity_admin___portrait_config_pb2___PortraitConfig: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        charset : typing___Optional[typing___Text] = None,
        user : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        config : typing___Optional[metadata_center_sdk___model___capacity_admin___portrait_config_pb2___PortraitConfig] = None,
        ctime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Portrait: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Portrait: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"config",b"config"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"charset",b"charset",u"config",b"config",u"creator",b"creator",u"ctime",b"ctime",u"instanceId",b"instanceId",u"memo",b"memo",u"name",b"name",u"user",b"user"]) -> None: ...
