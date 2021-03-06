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

from state_workflow_sdk.model.state_workflow.state_pb2 import (
    State as state_workflow_sdk___model___state_workflow___state_pb2___State,
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


class TransitStateWorkflowStatusRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    attribute = ... # type: typing___Text
    targetStateValue = ... # type: typing___Text

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        attribute : typing___Optional[typing___Text] = None,
        targetStateValue : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TransitStateWorkflowStatusRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TransitStateWorkflowStatusRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"attribute",b"attribute",u"instanceId",b"instanceId",u"objectId",b"objectId",u"targetStateValue",b"targetStateValue"]) -> None: ...

class TransitStateWorkflowStatusResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Transit(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class CurrentStateCallbacks(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            event = ... # type: typing___Text
            callbackUri = ... # type: typing___Text
            callbackServiceName = ... # type: typing___Text
            result = ... # type: builtin___bool

            def __init__(self,
                *,
                event : typing___Optional[typing___Text] = None,
                callbackUri : typing___Optional[typing___Text] = None,
                callbackServiceName : typing___Optional[typing___Text] = None,
                result : typing___Optional[builtin___bool] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> TransitStateWorkflowStatusResponse.Transit.CurrentStateCallbacks: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TransitStateWorkflowStatusResponse.Transit.CurrentStateCallbacks: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"callbackServiceName",b"callbackServiceName",u"callbackUri",b"callbackUri",u"event",b"event",u"result",b"result"]) -> None: ...

        class TargetStateCallbacks(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            event = ... # type: typing___Text
            callbackUri = ... # type: typing___Text
            callbackServiceName = ... # type: typing___Text
            result = ... # type: builtin___bool

            def __init__(self,
                *,
                event : typing___Optional[typing___Text] = None,
                callbackUri : typing___Optional[typing___Text] = None,
                callbackServiceName : typing___Optional[typing___Text] = None,
                result : typing___Optional[builtin___bool] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> TransitStateWorkflowStatusResponse.Transit.TargetStateCallbacks: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TransitStateWorkflowStatusResponse.Transit.TargetStateCallbacks: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"callbackServiceName",b"callbackServiceName",u"callbackUri",b"callbackUri",u"event",b"event",u"result",b"result"]) -> None: ...

        class TransitCallbacks(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            event = ... # type: typing___Text
            callbackUri = ... # type: typing___Text
            callbackServiceName = ... # type: typing___Text
            result = ... # type: builtin___bool

            def __init__(self,
                *,
                event : typing___Optional[typing___Text] = None,
                callbackUri : typing___Optional[typing___Text] = None,
                callbackServiceName : typing___Optional[typing___Text] = None,
                result : typing___Optional[builtin___bool] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> TransitStateWorkflowStatusResponse.Transit.TransitCallbacks: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TransitStateWorkflowStatusResponse.Transit.TransitCallbacks: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"callbackServiceName",b"callbackServiceName",u"callbackUri",b"callbackUri",u"event",b"event",u"result",b"result"]) -> None: ...


        @property
        def currentState(self) -> state_workflow_sdk___model___state_workflow___state_pb2___State: ...

        @property
        def currentStateCallbacks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TransitStateWorkflowStatusResponse.Transit.CurrentStateCallbacks]: ...

        @property
        def targetState(self) -> state_workflow_sdk___model___state_workflow___state_pb2___State: ...

        @property
        def targetStateCallbacks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TransitStateWorkflowStatusResponse.Transit.TargetStateCallbacks]: ...

        @property
        def transitCallbacks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[TransitStateWorkflowStatusResponse.Transit.TransitCallbacks]: ...

        def __init__(self,
            *,
            currentState : typing___Optional[state_workflow_sdk___model___state_workflow___state_pb2___State] = None,
            currentStateCallbacks : typing___Optional[typing___Iterable[TransitStateWorkflowStatusResponse.Transit.CurrentStateCallbacks]] = None,
            targetState : typing___Optional[state_workflow_sdk___model___state_workflow___state_pb2___State] = None,
            targetStateCallbacks : typing___Optional[typing___Iterable[TransitStateWorkflowStatusResponse.Transit.TargetStateCallbacks]] = None,
            transitCallbacks : typing___Optional[typing___Iterable[TransitStateWorkflowStatusResponse.Transit.TransitCallbacks]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> TransitStateWorkflowStatusResponse.Transit: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TransitStateWorkflowStatusResponse.Transit: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"currentState",b"currentState",u"targetState",b"targetState"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"currentState",b"currentState",u"currentStateCallbacks",b"currentStateCallbacks",u"targetState",b"targetState",u"targetStateCallbacks",b"targetStateCallbacks",u"transitCallbacks",b"transitCallbacks"]) -> None: ...

    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    attribute = ... # type: typing___Text

    @property
    def transit(self) -> TransitStateWorkflowStatusResponse.Transit: ...

    def __init__(self,
        *,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        attribute : typing___Optional[typing___Text] = None,
        transit : typing___Optional[TransitStateWorkflowStatusResponse.Transit] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TransitStateWorkflowStatusResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TransitStateWorkflowStatusResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"transit",b"transit"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"attribute",b"attribute",u"instanceId",b"instanceId",u"objectId",b"objectId",u"transit",b"transit"]) -> None: ...

class TransitStateWorkflowStatusResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> TransitStateWorkflowStatusResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[TransitStateWorkflowStatusResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> TransitStateWorkflowStatusResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> TransitStateWorkflowStatusResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
