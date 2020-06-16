# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from file_repository_sdk.model.file_repository.diff_pb2 import (
    Diff as file_repository_sdk___model___file_repository___diff_pb2___Diff,
)

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


class GetPackageDifferenceRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    package_from = ... # type: typing___Text
    package_to = ... # type: typing___Text
    ver_from = ... # type: typing___Text
    ver_to = ... # type: typing___Text
    diff_file = ... # type: typing___Text
    path = ... # type: typing___Text
    enconing = ... # type: typing___Text

    def __init__(self,
        *,
        package_from : typing___Optional[typing___Text] = None,
        package_to : typing___Optional[typing___Text] = None,
        ver_from : typing___Optional[typing___Text] = None,
        ver_to : typing___Optional[typing___Text] = None,
        diff_file : typing___Optional[typing___Text] = None,
        path : typing___Optional[typing___Text] = None,
        enconing : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetPackageDifferenceRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPackageDifferenceRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"diff_file",b"diff_file",u"enconing",b"enconing",u"package_from",b"package_from",u"package_to",b"package_to",u"path",b"path",u"ver_from",b"ver_from",u"ver_to",b"ver_to"]) -> None: ...

class GetPackageDifferenceResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> file_repository_sdk___model___file_repository___diff_pb2___Diff: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[file_repository_sdk___model___file_repository___diff_pb2___Diff] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetPackageDifferenceResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetPackageDifferenceResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
