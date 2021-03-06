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

from micro_app_sdk.model.micro_app.installed_micro_app_pb2 import (
    InstalledMicroApp as micro_app_sdk___model___micro_app___installed_micro_app_pb2___InstalledMicroApp,
)

from micro_app_sdk.model.micro_app.micro_app_container_pb2 import (
    MicroAppContainer as micro_app_sdk___model___micro_app___micro_app_container_pb2___MicroAppContainer,
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


class ListMicroAppContainerRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMicroAppContainerRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppContainerRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"page",b"page",u"page_size",b"page_size"]) -> None: ...

class ListMicroAppContainerResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        instanceId = ... # type: typing___Text
        name = ... # type: typing___Text
        id = ... # type: typing___Text
        type = ... # type: typing___Text
        order = ... # type: builtin___int

        @property
        def INSTALLED_MICRO_APP(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[micro_app_sdk___model___micro_app___installed_micro_app_pb2___InstalledMicroApp]: ...

        @property
        def children(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[micro_app_sdk___model___micro_app___micro_app_container_pb2___MicroAppContainer]: ...

        def __init__(self,
            *,
            INSTALLED_MICRO_APP : typing___Optional[typing___Iterable[micro_app_sdk___model___micro_app___installed_micro_app_pb2___InstalledMicroApp]] = None,
            children : typing___Optional[typing___Iterable[micro_app_sdk___model___micro_app___micro_app_container_pb2___MicroAppContainer]] = None,
            instanceId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            id : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            order : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListMicroAppContainerResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppContainerResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"INSTALLED_MICRO_APP",b"INSTALLED_MICRO_APP",u"children",b"children",u"id",b"id",u"instanceId",b"instanceId",u"name",b"name",u"order",b"order",u"type",b"type"]) -> None: ...

    total = ... # type: builtin___int
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListMicroAppContainerResponse.List]: ...

    def __init__(self,
        *,
        list : typing___Optional[typing___Iterable[ListMicroAppContainerResponse.List]] = None,
        total : typing___Optional[builtin___int] = None,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMicroAppContainerResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppContainerResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListMicroAppContainerResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListMicroAppContainerResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListMicroAppContainerResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListMicroAppContainerResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListMicroAppContainerResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
