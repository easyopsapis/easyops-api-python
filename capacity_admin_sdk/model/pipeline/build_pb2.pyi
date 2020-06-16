# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from capacity_admin_sdk.model.pipeline.build_status_pb2 import (
    BuildStatus as capacity_admin_sdk___model___pipeline___build_status_pb2___BuildStatus,
)

from capacity_admin_sdk.model.pipeline.git_meta_pb2 import (
    GitMeta as capacity_admin_sdk___model___pipeline___git_meta_pb2___GitMeta,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
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


class Build(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Artifact(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        packageName = ... # type: typing___Text
        versionName = ... # type: typing___Text
        ctime = ... # type: typing___Text
        packageId = ... # type: typing___Text
        versionId = ... # type: typing___Text

        def __init__(self,
            *,
            packageName : typing___Optional[typing___Text] = None,
            versionName : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[typing___Text] = None,
            packageId : typing___Optional[typing___Text] = None,
            versionId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Build.Artifact: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Build.Artifact: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"ctime",b"ctime",u"packageId",b"packageId",u"packageName",b"packageName",u"versionId",b"versionId",u"versionName",b"versionName"]) -> None: ...

    id = ... # type: typing___Text
    sender = ... # type: typing___Text
    created = ... # type: builtin___int
    yaml_string = ... # type: typing___Text
    number = ... # type: typing___Text
    events = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def git_meta(self) -> capacity_admin_sdk___model___pipeline___git_meta_pb2___GitMeta: ...

    @property
    def artifact(self) -> Build.Artifact: ...

    @property
    def status(self) -> capacity_admin_sdk___model___pipeline___build_status_pb2___BuildStatus: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        git_meta : typing___Optional[capacity_admin_sdk___model___pipeline___git_meta_pb2___GitMeta] = None,
        sender : typing___Optional[typing___Text] = None,
        artifact : typing___Optional[Build.Artifact] = None,
        created : typing___Optional[builtin___int] = None,
        yaml_string : typing___Optional[typing___Text] = None,
        status : typing___Optional[capacity_admin_sdk___model___pipeline___build_status_pb2___BuildStatus] = None,
        number : typing___Optional[typing___Text] = None,
        events : typing___Optional[typing___Iterable[typing___Text]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Build: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Build: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"artifact",b"artifact",u"git_meta",b"git_meta",u"status",b"status"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"artifact",b"artifact",u"created",b"created",u"events",b"events",u"git_meta",b"git_meta",u"id",b"id",u"number",b"number",u"sender",b"sender",u"status",b"status",u"yaml_string",b"yaml_string"]) -> None: ...
