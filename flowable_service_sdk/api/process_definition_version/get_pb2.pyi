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


class GetProcessDefinitionVersionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    definitionId = ... # type: typing___Text
    versionId = ... # type: typing___Text

    def __init__(self,
        *,
        definitionId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetProcessDefinitionVersionRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetProcessDefinitionVersionRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"definitionId",b"definitionId",u"versionId",b"versionId"]) -> None: ...

class GetProcessDefinitionVersionResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TaskInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        userTaskId = ... # type: typing___Text
        taskName = ... # type: typing___Text
        isSet = ... # type: builtin___bool
        formId = ... # type: typing___Text
        formName = ... # type: typing___Text
        formVersionId = ... # type: typing___Text
        formVersionName = ... # type: typing___Text
        taskWorkingTime = ... # type: typing___Text
        approvalLimit = ... # type: typing___Text

        def __init__(self,
            *,
            userTaskId : typing___Optional[typing___Text] = None,
            taskName : typing___Optional[typing___Text] = None,
            isSet : typing___Optional[builtin___bool] = None,
            formId : typing___Optional[typing___Text] = None,
            formName : typing___Optional[typing___Text] = None,
            formVersionId : typing___Optional[typing___Text] = None,
            formVersionName : typing___Optional[typing___Text] = None,
            taskWorkingTime : typing___Optional[typing___Text] = None,
            approvalLimit : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetProcessDefinitionVersionResponse.TaskInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetProcessDefinitionVersionResponse.TaskInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"approvalLimit",b"approvalLimit",u"formId",b"formId",u"formName",b"formName",u"formVersionId",b"formVersionId",u"formVersionName",b"formVersionName",u"isSet",b"isSet",u"taskName",b"taskName",u"taskWorkingTime",b"taskWorkingTime",u"userTaskId",b"userTaskId"]) -> None: ...

    vInstanceId = ... # type: typing___Text
    vCreator = ... # type: typing___Text
    vMemo = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    category = ... # type: typing___Text
    creator = ... # type: typing___Text
    memo = ... # type: typing___Text
    ctime = ... # type: typing___Text
    deploymentId = ... # type: typing___Text
    versionName = ... # type: typing___Text
    flowableDefinitionId = ... # type: typing___Text
    flowableDefinitionKey = ... # type: typing___Text
    isMain = ... # type: builtin___bool
    state = ... # type: typing___Text
    deploymentTime = ... # type: typing___Text
    parentDeploymentId = ... # type: typing___Text
    bpmnXML = ... # type: typing___Text

    @property
    def taskInfo(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetProcessDefinitionVersionResponse.TaskInfo]: ...

    def __init__(self,
        *,
        vInstanceId : typing___Optional[typing___Text] = None,
        vCreator : typing___Optional[typing___Text] = None,
        vMemo : typing___Optional[typing___Text] = None,
        taskInfo : typing___Optional[typing___Iterable[GetProcessDefinitionVersionResponse.TaskInfo]] = None,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        deploymentId : typing___Optional[typing___Text] = None,
        versionName : typing___Optional[typing___Text] = None,
        flowableDefinitionId : typing___Optional[typing___Text] = None,
        flowableDefinitionKey : typing___Optional[typing___Text] = None,
        isMain : typing___Optional[builtin___bool] = None,
        state : typing___Optional[typing___Text] = None,
        deploymentTime : typing___Optional[typing___Text] = None,
        parentDeploymentId : typing___Optional[typing___Text] = None,
        bpmnXML : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetProcessDefinitionVersionResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetProcessDefinitionVersionResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bpmnXML",b"bpmnXML",u"category",b"category",u"creator",b"creator",u"ctime",b"ctime",u"deploymentId",b"deploymentId",u"deploymentTime",b"deploymentTime",u"flowableDefinitionId",b"flowableDefinitionId",u"flowableDefinitionKey",b"flowableDefinitionKey",u"instanceId",b"instanceId",u"isMain",b"isMain",u"memo",b"memo",u"name",b"name",u"parentDeploymentId",b"parentDeploymentId",u"state",b"state",u"taskInfo",b"taskInfo",u"vCreator",b"vCreator",u"vInstanceId",b"vInstanceId",u"vMemo",b"vMemo",u"versionName",b"versionName"]) -> None: ...

class GetProcessDefinitionVersionResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> GetProcessDefinitionVersionResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[GetProcessDefinitionVersionResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetProcessDefinitionVersionResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetProcessDefinitionVersionResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
