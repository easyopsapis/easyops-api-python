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

from inspection_sdk.model.inspection.user_or_user_group_pb2 import (
    InspectionUserOrUserGroup as inspection_sdk___model___inspection___user_or_user_group_pb2___InspectionUserOrUserGroup,
)

from inspection_sdk.model.inspection.val_pb2 import (
    InspectionVal as inspection_sdk___model___inspection___val_pb2___InspectionVal,
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


class CreateTaskRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Args(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key = ... # type: typing___Text
        value = ... # type: typing___Text
        source = ... # type: typing___Text

        def __init__(self,
            *,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            source : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateTaskRequest.Args: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateTaskRequest.Args: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"key",b"key",u"source",b"source",u"value",b"value"]) -> None: ...

    class Targets(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text

        def __init__(self,
            *,
            instanceId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateTaskRequest.Targets: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateTaskRequest.Targets: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId"]) -> None: ...

    pluginId = ... # type: typing___Text
    name = ... # type: typing___Text
    isAllNotify = ... # type: builtin___bool
    notifyPassComparator = ... # type: typing___Text
    notifyScore = ... # type: builtin___float
    taskType = ... # type: typing___Text
    performanceTargets = ... # type: typing___Text
    queryStrategyId = ... # type: typing___Text
    taskScheduler = ... # type: typing___Text
    memo = ... # type: typing___Text
    templateId = ... # type: typing___Text
    templateName = ... # type: typing___Text

    @property
    def vals(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[inspection_sdk___model___inspection___val_pb2___InspectionVal]: ...

    @property
    def args(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateTaskRequest.Args]: ...

    @property
    def notifyUser(self) -> inspection_sdk___model___inspection___user_or_user_group_pb2___InspectionUserOrUserGroup: ...

    @property
    def notifyUserGroup(self) -> inspection_sdk___model___inspection___user_or_user_group_pb2___InspectionUserOrUserGroup: ...

    @property
    def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateTaskRequest.Targets]: ...

    def __init__(self,
        *,
        pluginId : typing___Optional[typing___Text] = None,
        vals : typing___Optional[typing___Iterable[inspection_sdk___model___inspection___val_pb2___InspectionVal]] = None,
        name : typing___Optional[typing___Text] = None,
        isAllNotify : typing___Optional[builtin___bool] = None,
        notifyPassComparator : typing___Optional[typing___Text] = None,
        notifyScore : typing___Optional[builtin___float] = None,
        args : typing___Optional[typing___Iterable[CreateTaskRequest.Args]] = None,
        notifyUser : typing___Optional[inspection_sdk___model___inspection___user_or_user_group_pb2___InspectionUserOrUserGroup] = None,
        notifyUserGroup : typing___Optional[inspection_sdk___model___inspection___user_or_user_group_pb2___InspectionUserOrUserGroup] = None,
        taskType : typing___Optional[typing___Text] = None,
        performanceTargets : typing___Optional[typing___Text] = None,
        queryStrategyId : typing___Optional[typing___Text] = None,
        taskScheduler : typing___Optional[typing___Text] = None,
        targets : typing___Optional[typing___Iterable[CreateTaskRequest.Targets]] = None,
        memo : typing___Optional[typing___Text] = None,
        templateId : typing___Optional[typing___Text] = None,
        templateName : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateTaskRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateTaskRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"notifyUser",b"notifyUser",u"notifyUserGroup",b"notifyUserGroup"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"args",b"args",u"isAllNotify",b"isAllNotify",u"memo",b"memo",u"name",b"name",u"notifyPassComparator",b"notifyPassComparator",u"notifyScore",b"notifyScore",u"notifyUser",b"notifyUser",u"notifyUserGroup",b"notifyUserGroup",u"performanceTargets",b"performanceTargets",u"pluginId",b"pluginId",u"queryStrategyId",b"queryStrategyId",u"targets",b"targets",u"taskScheduler",b"taskScheduler",u"taskType",b"taskType",u"templateId",b"templateId",u"templateName",b"templateName",u"vals",b"vals"]) -> None: ...

class CreateTaskResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Targets(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text

        def __init__(self,
            *,
            instanceId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateTaskResponse.Targets: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateTaskResponse.Targets: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId"]) -> None: ...

    name = ... # type: typing___Text
    taskScheduler = ... # type: typing___Text
    templateName = ... # type: typing___Text
    memo = ... # type: typing___Text
    taskType = ... # type: typing___Text

    @property
    def targets(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateTaskResponse.Targets]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        taskScheduler : typing___Optional[typing___Text] = None,
        templateName : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        taskType : typing___Optional[typing___Text] = None,
        targets : typing___Optional[typing___Iterable[CreateTaskResponse.Targets]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateTaskResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateTaskResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"memo",b"memo",u"name",b"name",u"targets",b"targets",u"taskScheduler",b"taskScheduler",u"taskType",b"taskType",u"templateName",b"templateName"]) -> None: ...

class CreateTaskResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> CreateTaskResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[CreateTaskResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateTaskResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateTaskResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
