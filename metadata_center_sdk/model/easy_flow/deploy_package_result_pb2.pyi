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

from metadata_center_sdk.model.easy_flow.package_info_pb2 import (
    PackageInfo as metadata_center_sdk___model___easy_flow___package_info_pb2___PackageInfo,
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


class DeployPackageResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Progress(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        msg = ... # type: typing___Text
        mtime = ... # type: typing___Text
        name = ... # type: typing___Text
        percent = ... # type: typing___Text
        status = ... # type: typing___Text
        values = ... # type: typing___Text

        def __init__(self,
            *,
            msg : typing___Optional[typing___Text] = None,
            mtime : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            percent : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            values : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> DeployPackageResult.Progress: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployPackageResult.Progress: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"msg",b"msg",u"mtime",b"mtime",u"name",b"name",u"percent",b"percent",u"status",b"status",u"values",b"values"]) -> None: ...

    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text
    installPath = ... # type: typing___Text
    usedTime = ... # type: builtin___int
    startTime = ... # type: typing___Text
    endTime = ... # type: typing___Text
    msg = ... # type: typing___Text
    status = ... # type: typing___Text
    code = ... # type: builtin___int

    @property
    def progress(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DeployPackageResult.Progress]: ...

    @property
    def param(self) -> metadata_center_sdk___model___easy_flow___package_info_pb2___PackageInfo: ...

    def __init__(self,
        *,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        installPath : typing___Optional[typing___Text] = None,
        usedTime : typing___Optional[builtin___int] = None,
        startTime : typing___Optional[typing___Text] = None,
        endTime : typing___Optional[typing___Text] = None,
        progress : typing___Optional[typing___Iterable[DeployPackageResult.Progress]] = None,
        msg : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        code : typing___Optional[builtin___int] = None,
        param : typing___Optional[metadata_center_sdk___model___easy_flow___package_info_pb2___PackageInfo] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> DeployPackageResult: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> DeployPackageResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"param",b"param"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"endTime",b"endTime",u"installPath",b"installPath",u"msg",b"msg",u"packageId",b"packageId",u"param",b"param",u"progress",b"progress",u"startTime",b"startTime",u"status",b"status",u"usedTime",b"usedTime",u"versionId",b"versionId"]) -> None: ...
