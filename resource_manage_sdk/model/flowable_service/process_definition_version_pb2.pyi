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

from resource_manage_sdk.model.flowable_service.bpmn_user_task_pb2 import (
    BPMNUserTask as resource_manage_sdk___model___flowable_service___bpmn_user_task_pb2___BPMNUserTask,
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


class ProcessDefinitionVersion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    versionName = ... # type: typing___Text
    deploymentId = ... # type: typing___Text
    flowableDefinitionId = ... # type: typing___Text
    flowableDefinitionKey = ... # type: typing___Text
    isMain = ... # type: builtin___bool
    state = ... # type: typing___Text
    deploymentTime = ... # type: typing___Text
    parentDeploymentId = ... # type: typing___Text
    bpmnXML = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    memo = ... # type: typing___Text

    @property
    def userTaskList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[resource_manage_sdk___model___flowable_service___bpmn_user_task_pb2___BPMNUserTask]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        versionName : typing___Optional[typing___Text] = None,
        deploymentId : typing___Optional[typing___Text] = None,
        flowableDefinitionId : typing___Optional[typing___Text] = None,
        flowableDefinitionKey : typing___Optional[typing___Text] = None,
        isMain : typing___Optional[builtin___bool] = None,
        state : typing___Optional[typing___Text] = None,
        deploymentTime : typing___Optional[typing___Text] = None,
        parentDeploymentId : typing___Optional[typing___Text] = None,
        bpmnXML : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        userTaskList : typing___Optional[typing___Iterable[resource_manage_sdk___model___flowable_service___bpmn_user_task_pb2___BPMNUserTask]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ProcessDefinitionVersion: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ProcessDefinitionVersion: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"bpmnXML",b"bpmnXML",u"creator",b"creator",u"ctime",b"ctime",u"deploymentId",b"deploymentId",u"deploymentTime",b"deploymentTime",u"flowableDefinitionId",b"flowableDefinitionId",u"flowableDefinitionKey",b"flowableDefinitionKey",u"instanceId",b"instanceId",u"isMain",b"isMain",u"memo",b"memo",u"name",b"name",u"parentDeploymentId",b"parentDeploymentId",u"state",b"state",u"userTaskList",b"userTaskList",u"versionName",b"versionName"]) -> None: ...
