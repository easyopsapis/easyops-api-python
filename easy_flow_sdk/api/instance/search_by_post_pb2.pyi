# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from easy_flow_sdk.model.easy_flow.instance_info_pb2 import (
    InstanceInfo as easy_flow_sdk___model___easy_flow___instance_info_pb2___InstanceInfo,
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


class PostSearchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    packageIds = ... # type: typing___Text
    deviceIds = ... # type: typing___Text
    deviceIp = ... # type: typing___Text
    appIds = ... # type: typing___Text
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int
    order = ... # type: typing___Text
    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text
    deviceId = ... # type: typing___Text
    appId = ... # type: typing___Text

    def __init__(self,
        *,
        packageIds : typing___Optional[typing___Text] = None,
        deviceIds : typing___Optional[typing___Text] = None,
        deviceIp : typing___Optional[typing___Text] = None,
        appIds : typing___Optional[typing___Text] = None,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        order : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        deviceId : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PostSearchRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PostSearchRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"appId",b"appId",u"appIds",b"appIds",u"deviceId",b"deviceId",u"deviceIds",b"deviceIds",u"deviceIp",b"deviceIp",u"order",b"order",u"packageId",b"packageId",u"packageIds",b"packageIds",u"page",b"page",u"pageSize",b"pageSize",u"versionId",b"versionId"]) -> None: ...

class PostSearchResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    total = ... # type: builtin___int
    page = ... # type: builtin___int
    pageSize = ... # type: builtin___int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[easy_flow_sdk___model___easy_flow___instance_info_pb2___InstanceInfo]: ...

    def __init__(self,
        *,
        total : typing___Optional[builtin___int] = None,
        list : typing___Optional[typing___Iterable[easy_flow_sdk___model___easy_flow___instance_info_pb2___InstanceInfo]] = None,
        page : typing___Optional[builtin___int] = None,
        pageSize : typing___Optional[builtin___int] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PostSearchResponse: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PostSearchResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"list",b"list",u"page",b"page",u"pageSize",b"pageSize",u"total",b"total"]) -> None: ...

class PostSearchResponseWrapper(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    code = ... # type: builtin___int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> PostSearchResponse: ...

    def __init__(self,
        *,
        code : typing___Optional[builtin___int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[PostSearchResponse] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> PostSearchResponseWrapper: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> PostSearchResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"codeExplain",b"codeExplain",u"data",b"data",u"error",b"error"]) -> None: ...
