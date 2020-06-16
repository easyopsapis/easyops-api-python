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

from tuna_service_sdk.model.micro_app.installed_micro_app_bootstrap_pb2 import (
    InstalledMicroAppBootstrap as tuna_service_sdk___model___micro_app___installed_micro_app_bootstrap_pb2___InstalledMicroAppBootstrap,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
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


class StoryBoard(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    dependsAll = ... # type: builtin___bool

    @property
    def app(self) -> tuna_service_sdk___model___micro_app___installed_micro_app_bootstrap_pb2___InstalledMicroAppBootstrap: ...

    @property
    def routes(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    @property
    def meta(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        *,
        app : typing___Optional[tuna_service_sdk___model___micro_app___installed_micro_app_bootstrap_pb2___InstalledMicroAppBootstrap] = None,
        dependsAll : typing___Optional[builtin___bool] = None,
        routes : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        meta : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StoryBoard: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StoryBoard: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"app",b"app",u"meta",b"meta"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"app",b"app",u"dependsAll",b"dependsAll",u"meta",b"meta",u"routes",b"routes"]) -> None: ...
