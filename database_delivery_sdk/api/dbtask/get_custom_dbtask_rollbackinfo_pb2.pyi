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


class GetCustomDBTaskRollbackInfoRequest(google___protobuf___message___Message):
    dbTaskId = ... # type: typing___Text

    def __init__(self,
        dbTaskId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomDBTaskRollbackInfoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"dbTaskId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"dbTaskId"]) -> None: ...

class GetCustomDBTaskRollbackInfoResponse(google___protobuf___message___Message):
    class ChangesetList(google___protobuf___message___Message):
        id = ... # type: typing___Text
        name = ... # type: typing___Text
        updateSql = ... # type: typing___Text
        rollbackSql = ... # type: typing___Text

        def __init__(self,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            updateSql : typing___Optional[typing___Text] = None,
            rollbackSql : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> GetCustomDBTaskRollbackInfoResponse.ChangesetList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"id",u"name",u"rollbackSql",u"updateSql"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"id",b"name",b"rollbackSql",b"updateSql"]) -> None: ...

    entityTaskId = ... # type: typing___Text
    dbInstanceId = ... # type: typing___Text
    dbInstanceName = ... # type: typing___Text

    @property
    def changesetList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetCustomDBTaskRollbackInfoResponse.ChangesetList]: ...

    def __init__(self,
        entityTaskId : typing___Optional[typing___Text] = None,
        dbInstanceId : typing___Optional[typing___Text] = None,
        dbInstanceName : typing___Optional[typing___Text] = None,
        changesetList : typing___Optional[typing___Iterable[GetCustomDBTaskRollbackInfoResponse.ChangesetList]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomDBTaskRollbackInfoResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"changesetList",u"dbInstanceId",u"dbInstanceName",u"entityTaskId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"changesetList",b"dbInstanceId",b"dbInstanceName",b"entityTaskId"]) -> None: ...

class GetCustomDBTaskRollbackInfoResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetCustomDBTaskRollbackInfoResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetCustomDBTaskRollbackInfoResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GetCustomDBTaskRollbackInfoResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...