# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
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
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class DebugCollectorRequest(google___protobuf___message___Message):
    class Args(google___protobuf___message___Message):
        key = ... # type: typing___Text
        value = ... # type: typing___Text

        def __init__(self,
            key : typing___Optional[typing___Text] = None,
            value : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DebugCollectorRequest.Args: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"key",u"value"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"key",b"value"]) -> None: ...

    pluginId = ... # type: typing___Text
    target = ... # type: typing___Text
    script = ... # type: typing___Text
    content = ... # type: typing___Text

    @property
    def args(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DebugCollectorRequest.Args]: ...

    def __init__(self,
        pluginId : typing___Optional[typing___Text] = None,
        target : typing___Optional[typing___Text] = None,
        args : typing___Optional[typing___Iterable[DebugCollectorRequest.Args]] = None,
        script : typing___Optional[typing___Text] = None,
        content : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DebugCollectorRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"args",u"content",u"pluginId",u"script",u"target"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"args",b"content",b"pluginId",b"script",b"target"]) -> None: ...

class DebugCollectorResponse(google___protobuf___message___Message):
    class MetricGroups(google___protobuf___message___Message):
        class DimStatus(google___protobuf___message___Message):
            status = ... # type: typing___Text
            id = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                status : typing___Optional[typing___Text] = None,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> DebugCollectorResponse.MetricGroups.DimStatus: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"id",u"name",u"status"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"id",b"name",b"status"]) -> None: ...

        class ValStatus(google___protobuf___message___Message):
            status = ... # type: typing___Text
            id = ... # type: typing___Text
            name = ... # type: typing___Text
            type = ... # type: typing___Text
            unit = ... # type: typing___Text

            def __init__(self,
                status : typing___Optional[typing___Text] = None,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                type : typing___Optional[typing___Text] = None,
                unit : typing___Optional[typing___Text] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> DebugCollectorResponse.MetricGroups.ValStatus: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"id",u"name",u"status",u"type",u"unit"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"id",b"name",b"status",b"type",b"unit"]) -> None: ...

        class List(google___protobuf___message___Message):
            class Dims(google___protobuf___message___Message):
                value = ... # type: typing___Text
                id = ... # type: typing___Text

                def __init__(self,
                    value : typing___Optional[typing___Text] = None,
                    id : typing___Optional[typing___Text] = None,
                    ) -> None: ...
                @classmethod
                def FromString(cls, s: bytes) -> DebugCollectorResponse.MetricGroups.List.Dims: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                if sys.version_info >= (3,):
                    def ClearField(self, field_name: typing_extensions___Literal[u"id",u"value"]) -> None: ...
                else:
                    def ClearField(self, field_name: typing_extensions___Literal[b"id",b"value"]) -> None: ...

            class Vals(google___protobuf___message___Message):
                value = ... # type: typing___Text
                id = ... # type: typing___Text

                def __init__(self,
                    value : typing___Optional[typing___Text] = None,
                    id : typing___Optional[typing___Text] = None,
                    ) -> None: ...
                @classmethod
                def FromString(cls, s: bytes) -> DebugCollectorResponse.MetricGroups.List.Vals: ...
                def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
                if sys.version_info >= (3,):
                    def ClearField(self, field_name: typing_extensions___Literal[u"id",u"value"]) -> None: ...
                else:
                    def ClearField(self, field_name: typing_extensions___Literal[b"id",b"value"]) -> None: ...


            @property
            def dims(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DebugCollectorResponse.MetricGroups.List.Dims]: ...

            @property
            def vals(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DebugCollectorResponse.MetricGroups.List.Vals]: ...

            def __init__(self,
                dims : typing___Optional[typing___Iterable[DebugCollectorResponse.MetricGroups.List.Dims]] = None,
                vals : typing___Optional[typing___Iterable[DebugCollectorResponse.MetricGroups.List.Vals]] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> DebugCollectorResponse.MetricGroups.List: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def ClearField(self, field_name: typing_extensions___Literal[u"dims",u"vals"]) -> None: ...
            else:
                def ClearField(self, field_name: typing_extensions___Literal[b"dims",b"vals"]) -> None: ...

        metric_group_status = ... # type: typing___Text
        id = ... # type: typing___Text
        name = ... # type: typing___Text
        category = ... # type: typing___Text

        @property
        def dim_status(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DebugCollectorResponse.MetricGroups.DimStatus]: ...

        @property
        def val_status(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DebugCollectorResponse.MetricGroups.ValStatus]: ...

        @property
        def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DebugCollectorResponse.MetricGroups.List]: ...

        def __init__(self,
            metric_group_status : typing___Optional[typing___Text] = None,
            dim_status : typing___Optional[typing___Iterable[DebugCollectorResponse.MetricGroups.DimStatus]] = None,
            val_status : typing___Optional[typing___Iterable[DebugCollectorResponse.MetricGroups.ValStatus]] = None,
            list : typing___Optional[typing___Iterable[DebugCollectorResponse.MetricGroups.List]] = None,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            category : typing___Optional[typing___Text] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> DebugCollectorResponse.MetricGroups: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"category",u"dim_status",u"id",u"list",u"metric_group_status",u"name",u"val_status"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"category",b"dim_status",b"id",b"list",b"metric_group_status",b"name",b"val_status"]) -> None: ...

    status = ... # type: typing___Text
    msg = ... # type: typing___Text

    @property
    def metric_groups(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[DebugCollectorResponse.MetricGroups]: ...

    def __init__(self,
        status : typing___Optional[typing___Text] = None,
        msg : typing___Optional[typing___Text] = None,
        metric_groups : typing___Optional[typing___Iterable[DebugCollectorResponse.MetricGroups]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DebugCollectorResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"metric_groups",u"msg",u"status"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"metric_groups",b"msg",b"status"]) -> None: ...

class DebugCollectorResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> DebugCollectorResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[DebugCollectorResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> DebugCollectorResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...