# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
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


class StartProcessInstanceRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class FormData(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        header = ... # type: typing___Text
        body = ... # type: typing___Text

        def __init__(self,
            *,
            header : typing___Optional[typing___Text] = None,
            body : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> StartProcessInstanceRequest.FormData: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StartProcessInstanceRequest.FormData: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"body",b"body",u"header",b"header"]) -> None: ...

    processVersionId = ... # type: typing___Text
    name = ... # type: typing___Text

    @property
    def formData(self) -> StartProcessInstanceRequest.FormData: ...

    def __init__(self,
        *,
        processVersionId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        formData : typing___Optional[StartProcessInstanceRequest.FormData] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StartProcessInstanceRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StartProcessInstanceRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"formData",b"formData"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"formData",b"formData",u"name",b"name",u"processVersionId",b"processVersionId"]) -> None: ...

class StartProcessInstanceResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class UserTaskList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        name = ... # type: typing___Text
        formDefinition = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            formDefinition : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> StartProcessInstanceResponse.UserTaskList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StartProcessInstanceResponse.UserTaskList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"formDefinition",b"formDefinition",u"id",b"id",u"name",b"name"]) -> None: ...

    class StepList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class FormData(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            header = ... # type: typing___Text
            body = ... # type: typing___Text

            def __init__(self,
                *,
                header : typing___Optional[typing___Text] = None,
                body : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> StartProcessInstanceResponse.StepList.FormData: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StartProcessInstanceResponse.StepList.FormData: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"body",b"body",u"header",b"header"]) -> None: ...

        userTaskId = ... # type: typing___Text
        assignee = ... # type: typing___Text

        @property
        def formData(self) -> StartProcessInstanceResponse.StepList.FormData: ...

        def __init__(self,
            *,
            userTaskId : typing___Optional[typing___Text] = None,
            assignee : typing___Optional[typing___Text] = None,
            formData : typing___Optional[StartProcessInstanceResponse.StepList.FormData] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> StartProcessInstanceResponse.StepList: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StartProcessInstanceResponse.StepList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"formData",b"formData"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"assignee",b"assignee",u"formData",b"formData",u"userTaskId",b"userTaskId"]) -> None: ...

    instanceId = ... # type: typing___Text
    flowableInstanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    etime = ... # type: typing___Text
    status = ... # type: typing___Text
    stepIdList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    stopAt = ... # type: typing___Text
    isSuspended = ... # type: builtin___bool
    isCancelled = ... # type: builtin___bool

    @property
    def userTaskList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StartProcessInstanceResponse.UserTaskList]: ...

    @property
    def stepList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StartProcessInstanceResponse.StepList]: ...

    def __init__(self,
        *,
        userTaskList : typing___Optional[typing___Iterable[StartProcessInstanceResponse.UserTaskList]] = None,
        stepList : typing___Optional[typing___Iterable[StartProcessInstanceResponse.StepList]] = None,
        instanceId : typing___Optional[typing___Text] = None,
        flowableInstanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        etime : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        stepIdList : typing___Optional[typing___Iterable[typing___Text]] = None,
        stopAt : typing___Optional[typing___Text] = None,
        isSuspended : typing___Optional[builtin___bool] = None,
        isCancelled : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StartProcessInstanceResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StartProcessInstanceResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"creator",b"creator",u"ctime",b"ctime",u"etime",b"etime",u"flowableInstanceId",b"flowableInstanceId",u"instanceId",b"instanceId",u"isCancelled",b"isCancelled",u"isSuspended",b"isSuspended",u"name",b"name",u"status",b"status",u"stepIdList",b"stepIdList",u"stepList",b"stepList",u"stopAt",b"stopAt",u"userTaskList",b"userTaskList"]) -> None: ...

class StartProcessInstanceResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> StartProcessInstanceResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[StartProcessInstanceResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StartProcessInstanceResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StartProcessInstanceResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
