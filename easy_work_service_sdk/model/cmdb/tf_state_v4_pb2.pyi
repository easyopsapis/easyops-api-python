# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
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


class TFStateV4(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Resources(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        mode = ... # type: typing___Text
        type = ... # type: typing___Text
        name = ... # type: typing___Text
        provider = ... # type: typing___Text

        @property
        def instances(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

        def __init__(self,
            *,
            mode : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            provider : typing___Optional[typing___Text] = None,
            instances : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> TFStateV4.Resources: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TFStateV4.Resources: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instances",b"instances",u"mode",b"mode",u"name",b"name",u"provider",b"provider",u"type",b"type"]) -> None: ...

    version = ... # type: builtin___int
    terraform_version = ... # type: typing___Text
    serial = ... # type: builtin___int
    lineage = ... # type: typing___Text

    @property
    def outputs(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def resources(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TFStateV4.Resources]: ...

    def __init__(self,
        *,
        version : typing___Optional[builtin___int] = None,
        terraform_version : typing___Optional[typing___Text] = None,
        serial : typing___Optional[builtin___int] = None,
        lineage : typing___Optional[typing___Text] = None,
        outputs : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        resources : typing___Optional[typing___Iterable[TFStateV4.Resources]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TFStateV4: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TFStateV4: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"outputs",b"outputs"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"lineage",b"lineage",u"outputs",b"outputs",u"resources",b"resources",u"serial",b"serial",u"terraform_version",b"terraform_version",u"version",b"version"]) -> None: ...