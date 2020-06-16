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

from state_workflow_sdk.model.state_workflow.stateWorkflow_pb2 import (
    StateWorkflow as state_workflow_sdk___model___state_workflow___stateWorkflow_pb2___StateWorkflow,
)

from state_workflow_sdk.model.state_workflow.state_pb2 import (
    State as state_workflow_sdk___model___state_workflow___state_pb2___State,
)

from state_workflow_sdk.model.state_workflow.transition_pb2 import (
    Transition as state_workflow_sdk___model___state_workflow___transition_pb2___Transition,
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


class CreateStateWorkflowRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ObjectInfo(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        objectId = ... # type: typing___Text
        attribute = ... # type: typing___Text
        filter = ... # type: typing___Text

        def __init__(self,
            *,
            objectId : typing___Optional[typing___Text] = None,
            attribute : typing___Optional[typing___Text] = None,
            filter : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateStateWorkflowRequest.ObjectInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateStateWorkflowRequest.ObjectInfo: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"attribute",b"attribute",u"filter",b"filter",u"objectId",b"objectId"]) -> None: ...

    class StateTriggers(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        event = ... # type: typing___Text
        id = ... # type: typing___Text
        callbackUri = ... # type: typing___Text
        callbackServiceName = ... # type: typing___Text

        def __init__(self,
            *,
            event : typing___Optional[typing___Text] = None,
            id : typing___Optional[typing___Text] = None,
            callbackUri : typing___Optional[typing___Text] = None,
            callbackServiceName : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateStateWorkflowRequest.StateTriggers: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateStateWorkflowRequest.StateTriggers: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"callbackServiceName",b"callbackServiceName",u"callbackUri",b"callbackUri",u"event",b"event",u"id",b"id"]) -> None: ...

    class TransitionTriggers(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        event = ... # type: typing___Text
        id = ... # type: typing___Text
        callbackUri = ... # type: typing___Text
        callbackServiceName = ... # type: typing___Text

        def __init__(self,
            *,
            event : typing___Optional[typing___Text] = None,
            id : typing___Optional[typing___Text] = None,
            callbackUri : typing___Optional[typing___Text] = None,
            callbackServiceName : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> CreateStateWorkflowRequest.TransitionTriggers: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateStateWorkflowRequest.TransitionTriggers: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"callbackServiceName",b"callbackServiceName",u"callbackUri",b"callbackUri",u"event",b"event",u"id",b"id"]) -> None: ...

    name = ... # type: typing___Text
    memo = ... # type: typing___Text

    @property
    def objectInfo(self) -> CreateStateWorkflowRequest.ObjectInfo: ...

    @property
    def states(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[state_workflow_sdk___model___state_workflow___state_pb2___State]: ...

    @property
    def stateTriggers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateStateWorkflowRequest.StateTriggers]: ...

    @property
    def transitions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[state_workflow_sdk___model___state_workflow___transition_pb2___Transition]: ...

    @property
    def transitionTriggers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[CreateStateWorkflowRequest.TransitionTriggers]: ...

    def __init__(self,
        *,
        name : typing___Optional[typing___Text] = None,
        objectInfo : typing___Optional[CreateStateWorkflowRequest.ObjectInfo] = None,
        states : typing___Optional[typing___Iterable[state_workflow_sdk___model___state_workflow___state_pb2___State]] = None,
        stateTriggers : typing___Optional[typing___Iterable[CreateStateWorkflowRequest.StateTriggers]] = None,
        transitions : typing___Optional[typing___Iterable[state_workflow_sdk___model___state_workflow___transition_pb2___Transition]] = None,
        transitionTriggers : typing___Optional[typing___Iterable[CreateStateWorkflowRequest.TransitionTriggers]] = None,
        memo : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateStateWorkflowRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateStateWorkflowRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"objectInfo",b"objectInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"memo",b"memo",u"name",b"name",u"objectInfo",b"objectInfo",u"stateTriggers",b"stateTriggers",u"states",b"states",u"transitionTriggers",b"transitionTriggers",u"transitions",b"transitions"]) -> None: ...

class CreateStateWorkflowResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> state_workflow_sdk___model___state_workflow___stateWorkflow_pb2___StateWorkflow: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[state_workflow_sdk___model___state_workflow___stateWorkflow_pb2___StateWorkflow] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> CreateStateWorkflowResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> CreateStateWorkflowResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...