# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.topology.view_pb2 import (
    View as model___topology___view_pb2___View,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListViewRequest(google___protobuf___message___Message):
    q = ... # type: typing___Text
    page = ... # type: int
    pageSize = ... # type: int

    def __init__(self,
        q : typing___Optional[typing___Text] = None,
        page : typing___Optional[int] = None,
        pageSize : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListViewRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"page",u"pageSize",u"q"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"page",b"pageSize",b"q"]) -> None: ...

class ListViewResponse(google___protobuf___message___Message):
    page = ... # type: int
    page_size = ... # type: int
    total = ... # type: int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___topology___view_pb2___View]: ...

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        total : typing___Optional[int] = None,
        list : typing___Optional[typing___Iterable[model___topology___view_pb2___View]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListViewResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"list",u"page",u"page_size",u"total"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"list",b"page",b"page_size",b"total"]) -> None: ...

class ListViewResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListViewResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListViewResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListViewResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...