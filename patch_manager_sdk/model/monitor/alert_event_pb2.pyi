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

from google.protobuf.struct_pb2 import (
    Value as google___protobuf___struct_pb2___Value,
)

from patch_manager_sdk.model.monitor.alert_conditions_pb2 import (
    AlertConditions as patch_manager_sdk___model___monitor___alert_conditions_pb2___AlertConditions,
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


class AlertEvent(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AlertReceivers(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        method = ... # type: typing___Text

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            method : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AlertEvent.AlertReceivers: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertEvent.AlertReceivers: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"method",b"method",u"name",b"name"]) -> None: ...

    class AlertDims(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text

        @property
        def value(self) -> google___protobuf___struct_pb2___Value: ...

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            value : typing___Optional[google___protobuf___struct_pb2___Value] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AlertEvent.AlertDims: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertEvent.AlertDims: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"value",b"value"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"value",b"value"]) -> None: ...

    class Actions(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Condition(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            lasting_for = ... # type: builtin___int
            level = ... # type: builtin___int

            def __init__(self,
                *,
                lasting_for : typing___Optional[builtin___int] = None,
                level : typing___Optional[builtin___int] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> AlertEvent.Actions.Condition: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertEvent.Actions.Condition: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"lasting_for",b"lasting_for",u"level",b"level"]) -> None: ...

        class ReceiverOwners(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            translate = ... # type: typing___Text
            object_id = ... # type: typing___Text
            object_attr_id = ... # type: typing___Text

            def __init__(self,
                *,
                translate : typing___Optional[typing___Text] = None,
                object_id : typing___Optional[typing___Text] = None,
                object_attr_id : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> AlertEvent.Actions.ReceiverOwners: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertEvent.Actions.ReceiverOwners: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"object_attr_id",b"object_attr_id",u"object_id",b"object_id",u"translate",b"translate"]) -> None: ...

        type = ... # type: typing___Text
        status = ... # type: builtin___int
        upgrade = ... # type: builtin___bool
        run = ... # type: builtin___bool
        methods = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        receivers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        receiver_user_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def condition(self) -> AlertEvent.Actions.Condition: ...

        @property
        def receiver_owners(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AlertEvent.Actions.ReceiverOwners]: ...

        def __init__(self,
            *,
            condition : typing___Optional[AlertEvent.Actions.Condition] = None,
            type : typing___Optional[typing___Text] = None,
            status : typing___Optional[builtin___int] = None,
            upgrade : typing___Optional[builtin___bool] = None,
            run : typing___Optional[builtin___bool] = None,
            methods : typing___Optional[typing___Iterable[typing___Text]] = None,
            receivers : typing___Optional[typing___Iterable[typing___Text]] = None,
            receiver_user_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
            receiver_owners : typing___Optional[typing___Iterable[AlertEvent.Actions.ReceiverOwners]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AlertEvent.Actions: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertEvent.Actions: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"condition",b"condition"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"condition",b"condition",u"methods",b"methods",u"receiver_owners",b"receiver_owners",u"receiver_user_groups",b"receiver_user_groups",u"receivers",b"receivers",u"run",b"run",u"status",b"status",u"type",b"type",u"upgrade",b"upgrade"]) -> None: ...

    id = ... # type: typing___Text
    alert_id = ... # type: typing___Text
    rule_id = ... # type: typing___Text
    is_recover = ... # type: builtin___bool
    send_succ = ... # type: builtin___bool
    subject = ... # type: typing___Text
    content = ... # type: typing___Text
    source = ... # type: typing___Text
    status = ... # type: builtin___int
    send_detail = ... # type: builtin___int
    recover_type = ... # type: typing___Text
    org = ... # type: builtin___int
    target = ... # type: typing___Text
    level = ... # type: builtin___int
    alert_duration = ... # type: builtin___float
    alert_begin_time = ... # type: builtin___int
    alert_end_time = ... # type: builtin___int
    time = ... # type: builtin___int
    start_time = ... # type: builtin___int
    insert_time = ... # type: builtin___int
    objectId = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    system = ... # type: typing___Text

    @property
    def value(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def alert_receivers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AlertEvent.AlertReceivers]: ...

    @property
    def alert_dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AlertEvent.AlertDims]: ...

    @property
    def actions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AlertEvent.Actions]: ...

    @property
    def alert_conditions(self) -> patch_manager_sdk___model___monitor___alert_conditions_pb2___AlertConditions: ...

    def __init__(self,
        *,
        id : typing___Optional[typing___Text] = None,
        alert_id : typing___Optional[typing___Text] = None,
        rule_id : typing___Optional[typing___Text] = None,
        is_recover : typing___Optional[builtin___bool] = None,
        send_succ : typing___Optional[builtin___bool] = None,
        subject : typing___Optional[typing___Text] = None,
        content : typing___Optional[typing___Text] = None,
        source : typing___Optional[typing___Text] = None,
        status : typing___Optional[builtin___int] = None,
        send_detail : typing___Optional[builtin___int] = None,
        recover_type : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        target : typing___Optional[typing___Text] = None,
        level : typing___Optional[builtin___int] = None,
        value : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        alert_duration : typing___Optional[builtin___float] = None,
        alert_begin_time : typing___Optional[builtin___int] = None,
        alert_end_time : typing___Optional[builtin___int] = None,
        time : typing___Optional[builtin___int] = None,
        start_time : typing___Optional[builtin___int] = None,
        insert_time : typing___Optional[builtin___int] = None,
        alert_receivers : typing___Optional[typing___Iterable[AlertEvent.AlertReceivers]] = None,
        alert_dims : typing___Optional[typing___Iterable[AlertEvent.AlertDims]] = None,
        actions : typing___Optional[typing___Iterable[AlertEvent.Actions]] = None,
        alert_conditions : typing___Optional[patch_manager_sdk___model___monitor___alert_conditions_pb2___AlertConditions] = None,
        objectId : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        system : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AlertEvent: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertEvent: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"alert_conditions",b"alert_conditions",u"value",b"value"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actions",b"actions",u"alert_begin_time",b"alert_begin_time",u"alert_conditions",b"alert_conditions",u"alert_dims",b"alert_dims",u"alert_duration",b"alert_duration",u"alert_end_time",b"alert_end_time",u"alert_id",b"alert_id",u"alert_receivers",b"alert_receivers",u"content",b"content",u"id",b"id",u"insert_time",b"insert_time",u"instanceId",b"instanceId",u"is_recover",b"is_recover",u"level",b"level",u"objectId",b"objectId",u"org",b"org",u"recover_type",b"recover_type",u"rule_id",b"rule_id",u"send_detail",b"send_detail",u"send_succ",b"send_succ",u"source",b"source",u"start_time",b"start_time",u"status",b"status",u"subject",b"subject",u"system",b"system",u"target",b"target",u"time",b"time",u"value",b"value"]) -> None: ...
