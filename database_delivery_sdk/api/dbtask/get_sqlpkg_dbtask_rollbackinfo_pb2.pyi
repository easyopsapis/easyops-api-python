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


class GetSQLPackageDBTaskRollbackInfoRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    dbTaskId = ... # type: typing___Text

    def __init__(self,
        *,
        dbTaskId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetSQLPackageDBTaskRollbackInfoRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetSQLPackageDBTaskRollbackInfoRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"dbTaskId",b"dbTaskId"]) -> None: ...

class GetSQLPackageDBTaskRollbackInfoResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class RollbackInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class ScriptInfo(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            id = ... # type: typing___Text
            updateName = ... # type: typing___Text
            rollbackName = ... # type: typing___Text

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                updateName : typing___Optional[typing___Text] = None,
                rollbackName : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo.ScriptInfo: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo.ScriptInfo: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"rollbackName",b"rollbackName",u"updateName",b"updateName"]) -> None: ...

        summaryTaskId = ... # type: typing___Text
        dbInstanceId = ... # type: typing___Text
        dbInstanceName = ... # type: typing___Text

        @property
        def scriptInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo.ScriptInfo]: ...

        def __init__(self,
            *,
            summaryTaskId : typing___Optional[typing___Text] = None,
            dbInstanceId : typing___Optional[typing___Text] = None,
            dbInstanceName : typing___Optional[typing___Text] = None,
            scriptInfo : typing___Optional[typing___Iterable[GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo.ScriptInfo]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"dbInstanceId",b"dbInstanceId",u"dbInstanceName",b"dbInstanceName",u"scriptInfo",b"scriptInfo",u"summaryTaskId",b"summaryTaskId"]) -> None: ...

    repoPackageId = ... # type: typing___Text
    repoVersionId = ... # type: typing___Text

    @property
    def rollbackInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo]: ...

    def __init__(self,
        *,
        repoPackageId : typing___Optional[typing___Text] = None,
        repoVersionId : typing___Optional[typing___Text] = None,
        rollbackInfo : typing___Optional[typing___Iterable[GetSQLPackageDBTaskRollbackInfoResponse.RollbackInfo]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetSQLPackageDBTaskRollbackInfoResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetSQLPackageDBTaskRollbackInfoResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"repoPackageId",b"repoPackageId",u"repoVersionId",b"repoVersionId",u"rollbackInfo",b"rollbackInfo"]) -> None: ...

class GetSQLPackageDBTaskRollbackInfoResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetSQLPackageDBTaskRollbackInfoResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetSQLPackageDBTaskRollbackInfoResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetSQLPackageDBTaskRollbackInfoResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetSQLPackageDBTaskRollbackInfoResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
