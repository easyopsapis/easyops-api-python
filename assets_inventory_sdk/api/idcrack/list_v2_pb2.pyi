# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from assets_inventory_sdk.model.assets_inventory.idc_pb2 import (
    InventoryIDC as assets_inventory_sdk___model___assets_inventory___idc_pb2___InventoryIDC,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
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


class ListIDCRackV2Request(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    idcrackIds = ... # type: typing___Text

    def __init__(self,
        *,
        idcrackIds : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListIDCRackV2Request: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListIDCRackV2Request: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"idcrackIds",b"idcrackIds"]) -> None: ...

class ListIDCRackV2Response(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Layout(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            instanceId = ... # type: typing___Text
            type = ... # type: typing___Text
            startU = ... # type: builtin___int
            occupiedU = ... # type: builtin___int

            @property
            def device(self) -> google___protobuf___struct_pb2___Struct: ...

            def __init__(self,
                *,
                instanceId : typing___Optional[typing___Text] = None,
                type : typing___Optional[typing___Text] = None,
                startU : typing___Optional[builtin___int] = None,
                occupiedU : typing___Optional[builtin___int] = None,
                device : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListIDCRackV2Response.List.Layout: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListIDCRackV2Response.List.Layout: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def HasField(self, field_name: typing_extensions___Literal[u"device",b"device"]) -> builtin___bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"device",b"device",u"instanceId",b"instanceId",u"occupiedU",b"occupiedU",u"startU",b"startU",u"type",b"type"]) -> None: ...

        instanceId = ... # type: typing___Text
        name = ... # type: typing___Text
        code = ... # type: typing___Text
        status = ... # type: typing___Text
        type = ... # type: typing___Text
        unum = ... # type: builtin___int
        freeUnum = ... # type: builtin___int
        ctime = ... # type: typing___Text
        creator = ... # type: typing___Text

        @property
        def layout(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListIDCRackV2Response.List.Layout]: ...

        @property
        def idc(self) -> assets_inventory_sdk___model___assets_inventory___idc_pb2___InventoryIDC: ...

        def __init__(self,
            *,
            layout : typing___Optional[typing___Iterable[ListIDCRackV2Response.List.Layout]] = None,
            idc : typing___Optional[assets_inventory_sdk___model___assets_inventory___idc_pb2___InventoryIDC] = None,
            instanceId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            code : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            unum : typing___Optional[builtin___int] = None,
            freeUnum : typing___Optional[builtin___int] = None,
            ctime : typing___Optional[typing___Text] = None,
            creator : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListIDCRackV2Response.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListIDCRackV2Response.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"idc",b"idc"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"creator",b"creator",u"ctime",b"ctime",u"freeUnum",b"freeUnum",u"idc",b"idc",u"instanceId",b"instanceId",u"layout",b"layout",u"name",b"name",u"status",b"status",u"type",b"type",u"unum",b"unum"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListIDCRackV2Response.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[ListIDCRackV2Response.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListIDCRackV2Response: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListIDCRackV2Response: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListIDCRackV2ResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListIDCRackV2Response: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListIDCRackV2Response] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListIDCRackV2ResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListIDCRackV2ResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
