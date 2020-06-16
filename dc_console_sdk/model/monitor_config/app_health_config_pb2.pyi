# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from dc_console_sdk.model.monitor_config.app_health_config_layer_pb2 import (
    AppHealthConfigLayer as dc_console_sdk___model___monitor_config___app_health_config_layer_pb2___AppHealthConfigLayer,
)

from dc_console_sdk.model.monitor_config.app_health_config_variable_pb2 import (
    AppHealthConfigVariable as dc_console_sdk___model___monitor_config___app_health_config_variable_pb2___AppHealthConfigVariable,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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


class AppHealthConfig(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    app_id = ... # type: typing___Text
    id = ... # type: typing___Text
    version_id = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: builtin___int
    modifier = ... # type: typing___Text
    mtime = ... # type: builtin___int
    org = ... # type: builtin___int

    @property
    def variables(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[dc_console_sdk___model___monitor_config___app_health_config_variable_pb2___AppHealthConfigVariable]: ...

    @property
    def layers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[dc_console_sdk___model___monitor_config___app_health_config_layer_pb2___AppHealthConfigLayer]: ...

    def __init__(self,
        *,
        app_id : typing___Optional[typing___Text] = None,
        id : typing___Optional[typing___Text] = None,
        version_id : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        modifier : typing___Optional[typing___Text] = None,
        mtime : typing___Optional[builtin___int] = None,
        org : typing___Optional[builtin___int] = None,
        variables : typing___Optional[typing___Iterable[dc_console_sdk___model___monitor_config___app_health_config_variable_pb2___AppHealthConfigVariable]] = None,
        layers : typing___Optional[typing___Iterable[dc_console_sdk___model___monitor_config___app_health_config_layer_pb2___AppHealthConfigLayer]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AppHealthConfig: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AppHealthConfig: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"app_id",b"app_id",u"creator",b"creator",u"ctime",b"ctime",u"id",b"id",u"layers",b"layers",u"modifier",b"modifier",u"mtime",b"mtime",u"org",b"org",u"variables",b"variables",u"version_id",b"version_id"]) -> None: ...
