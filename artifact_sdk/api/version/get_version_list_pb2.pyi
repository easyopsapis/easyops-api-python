# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.artifact.version_pb2 import (
    Version as model___artifact___version_pb2___Version,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class GetVersionListRequest(google___protobuf___message___Message):
    page = ... # type: int
    pageSize = ... # type: int
    order = ... # type: typing___Text
    XXX_RestFieldMask = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    packageId = ... # type: typing___Text
    env_type = ... # type: int
    name = ... # type: typing___Text

    def __init__(self,
        page : typing___Optional[int] = None,
        pageSize : typing___Optional[int] = None,
        order : typing___Optional[typing___Text] = None,
        XXX_RestFieldMask : typing___Optional[typing___Iterable[typing___Text]] = None,
        packageId : typing___Optional[typing___Text] = None,
        env_type : typing___Optional[int] = None,
        name : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetVersionListRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"XXX_RestFieldMask",u"env_type",u"name",u"order",u"packageId",u"page",u"pageSize"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"XXX_RestFieldMask",b"env_type",b"name",b"order",b"packageId",b"page",b"pageSize"]) -> None: ...

class GetVersionListResponse(google___protobuf___message___Message):
    page = ... # type: int
    page_size = ... # type: int
    total = ... # type: int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___artifact___version_pb2___Version]: ...

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        total : typing___Optional[int] = None,
        list : typing___Optional[typing___Iterable[model___artifact___version_pb2___Version]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetVersionListResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"list",u"page",u"page_size",u"total"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"list",b"page",b"page_size",b"total"]) -> None: ...

class GetVersionListResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetVersionListResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetVersionListResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetVersionListResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
