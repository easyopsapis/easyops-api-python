# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Value as google___protobuf___struct_pb2___Value,
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

from webshell_sdk.model.collector_center.script_pb2 import (
    Script as webshell_sdk___model___collector_center___script_pb2___Script,
)

from webshell_sdk.model.collector_center.target_range_pb2 import (
    TargetRange as webshell_sdk___model___collector_center___target_range_pb2___TargetRange,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode


class Configuration(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    org = ... # type: builtin___int
    id = ... # type: typing___Text
    name = ... # type: typing___Text
    timeout = ... # type: builtin___int
    disabled = ... # type: builtin___bool
    labels = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    ignoreInvalid = ... # type: builtin___bool
    interval = ... # type: builtin___int
    cacheTtl = ... # type: builtin___int
    timeRange = ... # type: typing___Text
    clazzId = ... # type: typing___Text
    clazzName = ... # type: typing___Text
    creator = ... # type: typing___Text
    modifier = ... # type: typing___Text
    ctime = ... # type: builtin___int
    mtime = ... # type: builtin___int
    objectId = ... # type: typing___Text
    instanceIdMacro = ... # type: typing___Text

    @property
    def kwargs(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def env(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def script(self) -> webshell_sdk___model___collector_center___script_pb2___Script: ...

    @property
    def targetRange(self) -> webshell_sdk___model___collector_center___target_range_pb2___TargetRange: ...

    def __init__(self,
        *,
        org : typing___Optional[builtin___int] = None,
        id : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        kwargs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        timeout : typing___Optional[builtin___int] = None,
        env : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        disabled : typing___Optional[builtin___bool] = None,
        labels : typing___Optional[typing___Iterable[typing___Text]] = None,
        ignoreInvalid : typing___Optional[builtin___bool] = None,
        script : typing___Optional[webshell_sdk___model___collector_center___script_pb2___Script] = None,
        targetRange : typing___Optional[webshell_sdk___model___collector_center___target_range_pb2___TargetRange] = None,
        interval : typing___Optional[builtin___int] = None,
        cacheTtl : typing___Optional[builtin___int] = None,
        timeRange : typing___Optional[typing___Text] = None,
        clazzId : typing___Optional[typing___Text] = None,
        clazzName : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        modifier : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        mtime : typing___Optional[builtin___int] = None,
        objectId : typing___Optional[typing___Text] = None,
        instanceIdMacro : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Configuration: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Configuration: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"env",b"env",u"kwargs",b"kwargs",u"script",b"script",u"targetRange",b"targetRange"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"cacheTtl",b"cacheTtl",u"clazzId",b"clazzId",u"clazzName",b"clazzName",u"creator",b"creator",u"ctime",b"ctime",u"disabled",b"disabled",u"env",b"env",u"id",b"id",u"ignoreInvalid",b"ignoreInvalid",u"instanceIdMacro",b"instanceIdMacro",u"interval",b"interval",u"kwargs",b"kwargs",u"labels",b"labels",u"modifier",b"modifier",u"mtime",b"mtime",u"name",b"name",u"objectId",b"objectId",u"org",b"org",u"script",b"script",u"targetRange",b"targetRange",u"timeRange",b"timeRange",u"timeout",b"timeout"]) -> None: ...
