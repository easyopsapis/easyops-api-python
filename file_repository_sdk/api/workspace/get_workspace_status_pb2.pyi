# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.file_repository.diff_pb2 import (
    Diff as model___file_repository___diff_pb2___Diff,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class StatusRequest(google___protobuf___message___Message):
    diff_file = ... # type: typing___Text
    path = ... # type: typing___Text
    encoding = ... # type: typing___Text
    packageId = ... # type: typing___Text

    def __init__(self,
        diff_file : typing___Optional[typing___Text] = None,
        path : typing___Optional[typing___Text] = None,
        encoding : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> StatusRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"diff_file",u"encoding",u"packageId",u"path"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"diff_file",b"encoding",b"packageId",b"path"]) -> None: ...

class StatusResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___file_repository___diff_pb2___Diff]: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[model___file_repository___diff_pb2___Diff]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> StatusResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
