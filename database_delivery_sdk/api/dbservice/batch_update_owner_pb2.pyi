# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.empty_pb2 import (
    Empty as google___protobuf___empty_pb2___Empty,
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class BatchUpdateDBServiceOwnerRequest(google___protobuf___message___Message):
    class UpdateDbservice(google___protobuf___message___Message):
        type = ... # type: typing___Text
        instanceIdList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        owner = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        def __init__(self,
            type : typing___Optional[typing___Text] = None,
            instanceIdList : typing___Optional[typing___Iterable[typing___Text]] = None,
            owner : typing___Optional[typing___Iterable[typing___Text]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> BatchUpdateDBServiceOwnerRequest.UpdateDbservice: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"instanceIdList",u"owner",u"type"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"instanceIdList",b"owner",b"type"]) -> None: ...


    @property
    def update_dbservice(self) -> BatchUpdateDBServiceOwnerRequest.UpdateDbservice: ...

    def __init__(self,
        update_dbservice : typing___Optional[BatchUpdateDBServiceOwnerRequest.UpdateDbservice] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BatchUpdateDBServiceOwnerRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"update_dbservice"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"update_dbservice"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"update_dbservice",b"update_dbservice"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"update_dbservice"]) -> None: ...

class BatchUpdateDBServiceOwnerResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___empty_pb2___Empty: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[google___protobuf___empty_pb2___Empty] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> BatchUpdateDBServiceOwnerResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...