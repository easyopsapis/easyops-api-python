# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from model.easy_flow.instance_info_pb2 import (
    InstanceInfo as model___easy_flow___instance_info_pb2___InstanceInfo,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class PostSearchRequest(google___protobuf___message___Message):
    packageIds = ... # type: typing___Text
    deviceIds = ... # type: typing___Text
    deviceIp = ... # type: typing___Text
    appIds = ... # type: typing___Text
    page = ... # type: int
    pageSize = ... # type: int
    order = ... # type: typing___Text
    packageId = ... # type: typing___Text
    versionId = ... # type: typing___Text
    deviceId = ... # type: typing___Text
    appId = ... # type: typing___Text

    def __init__(self,
        packageIds : typing___Optional[typing___Text] = None,
        deviceIds : typing___Optional[typing___Text] = None,
        deviceIp : typing___Optional[typing___Text] = None,
        appIds : typing___Optional[typing___Text] = None,
        page : typing___Optional[int] = None,
        pageSize : typing___Optional[int] = None,
        order : typing___Optional[typing___Text] = None,
        packageId : typing___Optional[typing___Text] = None,
        versionId : typing___Optional[typing___Text] = None,
        deviceId : typing___Optional[typing___Text] = None,
        appId : typing___Optional[typing___Text] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PostSearchRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"appId",u"appIds",u"deviceId",u"deviceIds",u"deviceIp",u"order",u"packageId",u"packageIds",u"page",u"pageSize",u"versionId"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"appId",b"appIds",b"deviceId",b"deviceIds",b"deviceIp",b"order",b"packageId",b"packageIds",b"page",b"pageSize",b"versionId"]) -> None: ...

class PostSearchResponse(google___protobuf___message___Message):
    page = ... # type: int
    page_size = ... # type: int
    total = ... # type: int

    @property
    def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___easy_flow___instance_info_pb2___InstanceInfo]: ...

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        total : typing___Optional[int] = None,
        list : typing___Optional[typing___Iterable[model___easy_flow___instance_info_pb2___InstanceInfo]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PostSearchResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"list",u"page",u"page_size",u"total"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[b"list",b"page",b"page_size",b"total"]) -> None: ...

class PostSearchResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> PostSearchResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[PostSearchResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PostSearchResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
