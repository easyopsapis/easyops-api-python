# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ImportInstanceRequest(google___protobuf___message___Message):
    objectId = ... # type: typing___Text
    keys = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

    @property
    def datas(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

    def __init__(self,
        objectId : typing___Optional[typing___Text] = None,
        keys : typing___Optional[typing___Iterable[typing___Text]] = None,
        datas : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ImportInstanceRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"datas",u"keys",u"objectId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"datas",b"keys",b"objectId"]) -> None: ...

class ImportInstanceResponse(google___protobuf___message___Message):
    class Data(google___protobuf___message___Message):
        code = ... # type: int
        error = ... # type: typing___Text

        @property
        def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___struct_pb2___Struct]: ...

        def __init__(self,
            code : typing___Optional[int] = None,
            error : typing___Optional[typing___Text] = None,
            data : typing___Optional[typing___Iterable[google___protobuf___struct_pb2___Struct]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ImportInstanceResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"code",u"data",u"error"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"code",b"data",b"error"]) -> None: ...

    insert_count = ... # type: int
    update_count = ... # type: int
    failed_count = ... # type: int

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ImportInstanceResponse.Data]: ...

    def __init__(self,
        insert_count : typing___Optional[int] = None,
        update_count : typing___Optional[int] = None,
        failed_count : typing___Optional[int] = None,
        data : typing___Optional[typing___Iterable[ImportInstanceResponse.Data]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ImportInstanceResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"data",u"failed_count",u"insert_count",u"update_count"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"data",b"failed_count",b"insert_count",b"update_count"]) -> None: ...

class ImportInstanceResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ImportInstanceResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ImportInstanceResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ImportInstanceResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
