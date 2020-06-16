# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from assets_inventory_sdk.model.monitor.alert_conditions_pb2 import (
    AlertConditions as assets_inventory_sdk___model___monitor___alert_conditions_pb2___AlertConditions,
)

from assets_inventory_sdk.model.monitor.alert_dims_pb2 import (
    AlertDims as assets_inventory_sdk___model___monitor___alert_dims_pb2___AlertDims,
)

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
    Struct as google___protobuf___struct_pb2___Struct,
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


class AlertRule(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
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
                def FromString(cls, s: builtin___bytes) -> AlertRule.Actions.Condition: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertRule.Actions.Condition: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"lasting_for",b"lasting_for",u"level",b"level"]) -> None: ...

        class ReceiverOwners(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            object_id = ... # type: typing___Text
            object_attr_id = ... # type: typing___Text
            translate = ... # type: typing___Text

            def __init__(self,
                *,
                object_id : typing___Optional[typing___Text] = None,
                object_attr_id : typing___Optional[typing___Text] = None,
                translate : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> AlertRule.Actions.ReceiverOwners: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertRule.Actions.ReceiverOwners: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"object_attr_id",b"object_attr_id",u"object_id",b"object_id",u"translate",b"translate"]) -> None: ...

        type = ... # type: typing___Text
        upgrade = ... # type: builtin___bool
        methods = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        receivers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
        receiver_user_groups = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def condition(self) -> AlertRule.Actions.Condition: ...

        @property
        def receiver_owners(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AlertRule.Actions.ReceiverOwners]: ...

        def __init__(self,
            *,
            condition : typing___Optional[AlertRule.Actions.Condition] = None,
            type : typing___Optional[typing___Text] = None,
            upgrade : typing___Optional[builtin___bool] = None,
            methods : typing___Optional[typing___Iterable[typing___Text]] = None,
            receivers : typing___Optional[typing___Iterable[typing___Text]] = None,
            receiver_user_groups : typing___Optional[typing___Iterable[typing___Text]] = None,
            receiver_owners : typing___Optional[typing___Iterable[AlertRule.Actions.ReceiverOwners]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AlertRule.Actions: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertRule.Actions: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"condition",b"condition"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"condition",b"condition",u"methods",b"methods",u"receiver_owners",b"receiver_owners",u"receiver_user_groups",b"receiver_user_groups",u"receivers",b"receivers",u"type",b"type",u"upgrade",b"upgrade"]) -> None: ...

    class Templates(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        content_template = ... # type: typing___Text
        target_template = ... # type: typing___Text
        recovery_content_template = ... # type: typing___Text

        def __init__(self,
            *,
            content_template : typing___Optional[typing___Text] = None,
            target_template : typing___Optional[typing___Text] = None,
            recovery_content_template : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AlertRule.Templates: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertRule.Templates: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"content_template",b"content_template",u"recovery_content_template",b"recovery_content_template",u"target_template",b"target_template"]) -> None: ...

    class Instances(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        type = ... # type: typing___Text
        instanceIds = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]

        @property
        def query(self) -> google___protobuf___struct_pb2___Struct: ...

        def __init__(self,
            *,
            type : typing___Optional[typing___Text] = None,
            instanceIds : typing___Optional[typing___Iterable[typing___Text]] = None,
            query : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> AlertRule.Instances: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertRule.Instances: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"query",b"query"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceIds",b"instanceIds",u"query",b"query",u"type",b"type"]) -> None: ...

    org = ... # type: builtin___int
    id = ... # type: typing___Text
    rule_name = ... # type: typing___Text
    version = ... # type: builtin___int
    version_id = ... # type: typing___Text
    rule_priority = ... # type: builtin___int
    detect_window = ... # type: builtin___int
    alert_count = ... # type: builtin___int
    alert_interval = ... # type: builtin___int
    recover_count = ... # type: builtin___int
    creator = ... # type: typing___Text
    ctime = ... # type: builtin___int
    mtime = ... # type: builtin___int
    objectId = ... # type: typing___Text
    disabled = ... # type: builtin___bool
    source = ... # type: typing___Text

    @property
    def alert_dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[assets_inventory_sdk___model___monitor___alert_dims_pb2___AlertDims]: ...

    @property
    def alert_conditions(self) -> assets_inventory_sdk___model___monitor___alert_conditions_pb2___AlertConditions: ...

    @property
    def actions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[AlertRule.Actions]: ...

    @property
    def templates(self) -> AlertRule.Templates: ...

    @property
    def instances(self) -> AlertRule.Instances: ...

    def __init__(self,
        *,
        org : typing___Optional[builtin___int] = None,
        id : typing___Optional[typing___Text] = None,
        rule_name : typing___Optional[typing___Text] = None,
        version : typing___Optional[builtin___int] = None,
        version_id : typing___Optional[typing___Text] = None,
        alert_dims : typing___Optional[typing___Iterable[assets_inventory_sdk___model___monitor___alert_dims_pb2___AlertDims]] = None,
        rule_priority : typing___Optional[builtin___int] = None,
        alert_conditions : typing___Optional[assets_inventory_sdk___model___monitor___alert_conditions_pb2___AlertConditions] = None,
        detect_window : typing___Optional[builtin___int] = None,
        alert_count : typing___Optional[builtin___int] = None,
        alert_interval : typing___Optional[builtin___int] = None,
        recover_count : typing___Optional[builtin___int] = None,
        actions : typing___Optional[typing___Iterable[AlertRule.Actions]] = None,
        templates : typing___Optional[AlertRule.Templates] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[builtin___int] = None,
        mtime : typing___Optional[builtin___int] = None,
        instances : typing___Optional[AlertRule.Instances] = None,
        objectId : typing___Optional[typing___Text] = None,
        disabled : typing___Optional[builtin___bool] = None,
        source : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> AlertRule: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> AlertRule: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"alert_conditions",b"alert_conditions",u"instances",b"instances",u"templates",b"templates"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"actions",b"actions",u"alert_conditions",b"alert_conditions",u"alert_count",b"alert_count",u"alert_dims",b"alert_dims",u"alert_interval",b"alert_interval",u"creator",b"creator",u"ctime",b"ctime",u"detect_window",b"detect_window",u"disabled",b"disabled",u"id",b"id",u"instances",b"instances",u"mtime",b"mtime",u"objectId",b"objectId",u"org",b"org",u"recover_count",b"recover_count",u"rule_name",b"rule_name",u"rule_priority",b"rule_priority",u"source",b"source",u"templates",b"templates",u"version",b"version",u"version_id",b"version_id"]) -> None: ...
