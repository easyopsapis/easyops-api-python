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
    page = ... # type: builtin___int
    page_size = ... # type: builtin___int

    def __init__(self,
        *,
        page : typing___Optional[builtin___int] = None,
        page_size : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ListRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"page",b"page",u"page_size",b"page_size"]) -> None: ...

class ListResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class List(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class NamespaceList(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            instanceId = ... # type: typing___Text
            resourceName = ... # type: typing___Text

            def __init__(self,
                *,
                instanceId : typing___Optional[typing___Text] = None,
                resourceName : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListResponse.List.NamespaceList: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse.List.NamespaceList: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"resourceName",b"resourceName"]) -> None: ...

        class ResourceGroupList(google___protobuf___message___Message):
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
                def FromString(cls, s: builtin___bytes) -> ListResponse.List.ResourceGroupList: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse.List.ResourceGroupList: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"name",b"name"]) -> None: ...

        class AuthInfo(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            username = ... # type: typing___Text
            password = ... # type: typing___Text

            def __init__(self,
                *,
                username : typing___Optional[typing___Text] = None,
                password : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListResponse.List.AuthInfo: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse.List.AuthInfo: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"password",b"password",u"username",b"username"]) -> None: ...

        class TlsConfig(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            clientCertificate = ... # type: typing___Text
            clientKey = ... # type: typing___Text
            clusterCA = ... # type: typing___Text

            def __init__(self,
                *,
                clientCertificate : typing___Optional[typing___Text] = None,
                clientKey : typing___Optional[typing___Text] = None,
                clusterCA : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> ListResponse.List.TlsConfig: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse.List.TlsConfig: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"clientCertificate",b"clientCertificate",u"clientKey",b"clientKey",u"clusterCA",b"clusterCA"]) -> None: ...

        instanceId = ... # type: typing___Text
        name = ... # type: typing___Text
        host = ... # type: typing___Text
        environment = ... # type: typing___Text
        authMode = ... # type: typing___Text
        defaultStorageClass = ... # type: typing___Text
        description = ... # type: typing___Text
        provider = ... # type: typing___Text
        zone = ... # type: typing___Text
        zoneId = ... # type: typing___Text
        cloudProvider = ... # type: typing___Text
        ctime = ... # type: typing___Text

        @property
        def namespaceList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListResponse.List.NamespaceList]: ...

        @property
        def resourceGroupList(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListResponse.List.ResourceGroupList]: ...

        @property
        def authInfo(self) -> ListResponse.List.AuthInfo: ...

        @property
        def tlsConfig(self) -> ListResponse.List.TlsConfig: ...

        def __init__(self,
            *,
            namespaceList : typing___Optional[typing___Iterable[ListResponse.List.NamespaceList]] = None,
            resourceGroupList : typing___Optional[typing___Iterable[ListResponse.List.ResourceGroupList]] = None,
            instanceId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            host : typing___Optional[typing___Text] = None,
            environment : typing___Optional[typing___Text] = None,
            authMode : typing___Optional[typing___Text] = None,
            authInfo : typing___Optional[ListResponse.List.AuthInfo] = None,
            tlsConfig : typing___Optional[ListResponse.List.TlsConfig] = None,
            defaultStorageClass : typing___Optional[typing___Text] = None,
            description : typing___Optional[typing___Text] = None,
            provider : typing___Optional[typing___Text] = None,
            zone : typing___Optional[typing___Text] = None,
            zoneId : typing___Optional[typing___Text] = None,
            cloudProvider : typing___Optional[typing___Text] = None,
            ctime : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> ListResponse.List: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> ListResponse.List: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"authInfo",b"authInfo",u"tlsConfig",b"tlsConfig"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"authInfo",b"authInfo",u"authMode",b"authMode",u"cloudProvider",b"cloudProvider",u"ctime",b"ctime",u"defaultStorageClass",b"defaultStorageClass",u"description",b"description",u"environment",b"environment",u"host",b"host",u"instanceId",b"instanceId",u"name",b"name",u"namespaceList",b"namespaceList",u"provider",b"provider",u"resourceGroupList",b"resourceGroupList",u"tlsConfig",b"tlsConfig",u"zone",b"zone",u"zoneId",b"zoneId"]) -> None: ...

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
