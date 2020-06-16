# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from architecture_view_sdk.model.easy_command.action_param_custom_pb2 import (
    ActionParamCustom as architecture_view_sdk___model___easy_command___action_param_custom_pb2___ActionParamCustom,
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


class Target(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    targetId = ... # type: typing___Text
    targetName = ... # type: typing___Text

    @property
    def actionParams(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[architecture_view_sdk___model___easy_command___action_param_custom_pb2___ActionParamCustom]: ...

    def __init__(self,
        *,
        targetId : typing___Optional[typing___Text] = None,
        targetName : typing___Optional[typing___Text] = None,
        actionParams : typing___Optional[typing___Iterable[architecture_view_sdk___model___easy_command___action_param_custom_pb2___ActionParamCustom]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Target: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Target: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actionParams",b"actionParams",u"targetId",b"targetId",u"targetName",b"targetName"]) -> None: ...