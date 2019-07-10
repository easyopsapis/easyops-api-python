# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListSupportInformResponse(google___protobuf___message___Message):
    class Data(google___protobuf___message___Message):
        col_of_cmdb_user_object = ... # type: typing___Text
        enable = ... # type: typing___Text
        plugin_name = ... # type: typing___Text
        description = ... # type: typing___Text
        inform_type = ... # type: typing___Text

        def __init__(self,
            col_of_cmdb_user_object : typing___Optional[typing___Text] = None,
            enable : typing___Optional[typing___Text] = None,
            plugin_name : typing___Optional[typing___Text] = None,
            description : typing___Optional[typing___Text] = None,
            inform_type : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListSupportInformResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"col_of_cmdb_user_object",u"description",u"enable",u"inform_type",u"plugin_name"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"col_of_cmdb_user_object",b"description",b"enable",b"inform_type",b"plugin_name"]) -> None: ...

    page = ... # type: int
    page_size = ... # type: int
    tatal = ... # type: int
    msg = ... # type: typing___Text
    code = ... # type: int

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListSupportInformResponse.Data]: ...

    def __init__(self,
        data : typing___Optional[typing___Iterable[ListSupportInformResponse.Data]] = None,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        tatal : typing___Optional[int] = None,
        msg : typing___Optional[typing___Text] = None,
        code : typing___Optional[int] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListSupportInformResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"data",u"msg",u"page",u"page_size",u"tatal"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"data",b"msg",b"page",b"page_size",b"tatal"]) -> None: ...

class ListSupportInformResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListSupportInformResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListSupportInformResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListSupportInformResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
