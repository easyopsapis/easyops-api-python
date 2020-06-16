# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from patch_manager_sdk.model.ops_automation.bind_resource_pb2 import (
    BindResource as patch_manager_sdk___model___ops_automation___bind_resource_pb2___BindResource,
)

from patch_manager_sdk.model.ops_automation.mail_info_pb2 import (
    MailInfo as patch_manager_sdk___model___ops_automation___mail_info_pb2___MailInfo,
)

from typing import (
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


class JobDetails(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Scheduler(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        isBound = ... # type: builtin___bool
        isActive = ... # type: builtin___bool

        def __init__(self,
            *,
            isBound : typing___Optional[builtin___bool] = None,
            isActive : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> JobDetails.Scheduler: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> JobDetails.Scheduler: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"isActive",b"isActive",u"isBound",b"isBound"]) -> None: ...

    version = ... # type: builtin___int
    createTime = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    creator = ... # type: typing___Text
    org = ... # type: builtin___int
    name = ... # type: typing___Text
    category = ... # type: typing___Text
    menuId = ... # type: typing___Text
    desc = ... # type: typing___Text
    allowModify = ... # type: builtin___bool
    id = ... # type: typing___Text

    @property
    def scheduler(self) -> JobDetails.Scheduler: ...

    @property
    def bindResource(self) -> patch_manager_sdk___model___ops_automation___bind_resource_pb2___BindResource: ...

    @property
    def mail(self) -> patch_manager_sdk___model___ops_automation___mail_info_pb2___MailInfo: ...

    def __init__(self,
        *,
        version : typing___Optional[builtin___int] = None,
        createTime : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        scheduler : typing___Optional[JobDetails.Scheduler] = None,
        name : typing___Optional[typing___Text] = None,
        category : typing___Optional[typing___Text] = None,
        menuId : typing___Optional[typing___Text] = None,
        bindResource : typing___Optional[patch_manager_sdk___model___ops_automation___bind_resource_pb2___BindResource] = None,
        desc : typing___Optional[typing___Text] = None,
        allowModify : typing___Optional[builtin___bool] = None,
        mail : typing___Optional[patch_manager_sdk___model___ops_automation___mail_info_pb2___MailInfo] = None,
        id : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> JobDetails: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> JobDetails: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"bindResource",b"bindResource",u"mail",b"mail",u"scheduler",b"scheduler"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"allowModify",b"allowModify",u"bindResource",b"bindResource",u"category",b"category",u"createTime",b"createTime",u"creator",b"creator",u"desc",b"desc",u"id",b"id",u"mail",b"mail",u"menuId",b"menuId",u"name",b"name",u"org",b"org",u"scheduler",b"scheduler",u"updateTime",b"updateTime",u"version",b"version"]) -> None: ...
