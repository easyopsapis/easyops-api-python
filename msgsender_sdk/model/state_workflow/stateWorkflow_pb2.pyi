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

from msgsender_sdk.model.state_workflow.state_pb2 import (
    State as msgsender_sdk___model___state_workflow___state_pb2___State,
)

from msgsender_sdk.model.state_workflow.transition_pb2 import (
    Transition as msgsender_sdk___model___state_workflow___transition_pb2___Transition,
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


class StateWorkflow(google___protobuf___message___Message):
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
            def FromString(cls, s: builtin___bytes) -> StateWorkflow.ObjectInfo: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StateWorkflow.ObjectInfo: ...
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
            def FromString(cls, s: builtin___bytes) -> StateWorkflow.StateTriggers: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StateWorkflow.StateTriggers: ...
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
            def FromString(cls, s: builtin___bytes) -> StateWorkflow.TransitionTriggers: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StateWorkflow.TransitionTriggers: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"callbackServiceName",b"callbackServiceName",u"callbackUri",b"callbackUri",u"event",b"event",u"id",b"id"]) -> None: ...

    instanceId = ... # type: typing___Text
    name = ... # type: typing___Text
    memo = ... # type: typing___Text

    @property
    def objectInfo(self) -> StateWorkflow.ObjectInfo: ...

    @property
    def states(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[msgsender_sdk___model___state_workflow___state_pb2___State]: ...

    @property
    def stateTriggers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StateWorkflow.StateTriggers]: ...

    @property
    def transitions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[msgsender_sdk___model___state_workflow___transition_pb2___Transition]: ...

    @property
    def transitionTriggers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[StateWorkflow.TransitionTriggers]: ...

    def __init__(self,
        *,
        instanceId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        objectInfo : typing___Optional[StateWorkflow.ObjectInfo] = None,
        states : typing___Optional[typing___Iterable[msgsender_sdk___model___state_workflow___state_pb2___State]] = None,
        stateTriggers : typing___Optional[typing___Iterable[StateWorkflow.StateTriggers]] = None,
        transitions : typing___Optional[typing___Iterable[msgsender_sdk___model___state_workflow___transition_pb2___Transition]] = None,
        transitionTriggers : typing___Optional[typing___Iterable[StateWorkflow.TransitionTriggers]] = None,
        memo : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> StateWorkflow: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> StateWorkflow: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"objectInfo",b"objectInfo"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"memo",b"memo",u"name",b"name",u"objectInfo",b"objectInfo",u"stateTriggers",b"stateTriggers",u"states",b"states",u"transitionTriggers",b"transitionTriggers",u"transitions",b"transitions"]) -> None: ...
