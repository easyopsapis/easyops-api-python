# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from container_sdk.model.container.cluster_pb2 import (
    Cluster as container_sdk___model___container___cluster_pb2___Cluster,
)

from container_sdk.model.container.hpa_pb2 import (
    HorizontalPodAutoscaler as container_sdk___model___container___hpa_pb2___HorizontalPodAutoscaler,
)

from container_sdk.model.container.namespace_pb2 import (
    Namespace as container_sdk___model___container___namespace_pb2___Namespace,
)

from container_sdk.model.container.resource_group_pb2 import (
    ResourceGroup as container_sdk___model___container___resource_group_pb2___ResourceGroup,
)

from container_sdk.model.container.workload_pb2 import (
    Workload as container_sdk___model___container___workload_pb2___Workload,
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


class ListRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    clusterId = ... # type: typing___Text
    workspaceId = ... # type: typing___Text
    namespaceId = ... # type: typing___Text
    resourceGroupName = ... # type: typing___Text
    workloadState = ... # type: typing___Text
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    sort = ... # type: typing___Text
    order = ... # type: builtin___int

    def __init__(self,
        *,
        clusterId : typing___Optional[typing___Text] = None,
        workspaceId : typing___Optional[typing___Text] = None,
        namespaceId : typing___Optional[typing___Text] = None,
        resourceGroupName : typing___Optional[typing___Text] = None,
        workloadState : typing___Optional[typing___Text] = None,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        sort : typing___Optional[typing___Text] = None,
        order : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"clusterId",b"clusterId",u"namespaceId",b"namespaceId",u"order",b"order",u"page",b"page",u"page_size",b"page_size",u"resourceGroupName",b"resourceGroupName",u"sort",b"sort",u"workloadState",b"workloadState",u"workspaceId",b"workspaceId"]) -> None: ...

class ListResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class App(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            instanceId = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                *,
                instanceId : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListResponse.List.App: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse.List.App: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"name",b"name"]) -> None: ...


        @property
        def resourcegroup(self) -> container_sdk___model___container___resource_group_pb2___ResourceGroup: ...

        @property
        def namespace(self) -> container_sdk___model___container___namespace_pb2___Namespace: ...

        @property
        def workload(self) -> container_sdk___model___container___workload_pb2___Workload: ...

        @property
        def hpa(self) -> container_sdk___model___container___hpa_pb2___HorizontalPodAutoscaler: ...

        @property
        def cluster(self) -> container_sdk___model___container___cluster_pb2___Cluster: ...

        @property
        def app(self) -> ListResponse.List.App: ...

        def __init__(self,
            *,
            resourcegroup : typing___Optional[container_sdk___model___container___resource_group_pb2___ResourceGroup] = None,
            namespace : typing___Optional[container_sdk___model___container___namespace_pb2___Namespace] = None,
            workload : typing___Optional[container_sdk___model___container___workload_pb2___Workload] = None,
            hpa : typing___Optional[container_sdk___model___container___hpa_pb2___HorizontalPodAutoscaler] = None,
            cluster : typing___Optional[container_sdk___model___container___cluster_pb2___Cluster] = None,
            app : typing___Optional[ListResponse.List.App] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"app",b"app",u"cluster",b"cluster",u"hpa",b"hpa",u"namespace",b"namespace",u"resourcegroup",b"resourcegroup",u"workload",b"workload"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"app",b"app",u"cluster",b"cluster",u"hpa",b"hpa",u"namespace",b"namespace",u"resourcegroup",b"resourcegroup",u"workload",b"workload"]) -> None: ...

    page = ... # type: builtin___int
    page_size = ... # type: builtin___int
    total = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListResponse.List]: ...

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[ListResponse.List]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"page_size",b"page_size",u"total",b"total"]) -> None: ...

class ListResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
