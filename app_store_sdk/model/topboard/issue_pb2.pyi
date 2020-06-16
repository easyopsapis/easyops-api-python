# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from app_store_sdk.model.cmdb.user_pb2 import (
    User as app_store_sdk___model___cmdb___user_pb2___User,
)

from app_store_sdk.model.topboard.attachment_pb2 import (
    Attachment as app_store_sdk___model___topboard___attachment_pb2___Attachment,
)

from app_store_sdk.model.topboard.comment_pb2 import (
    Comment as app_store_sdk___model___topboard___comment_pb2___Comment,
)

from app_store_sdk.model.topboard.product_pb2 import (
    Product as app_store_sdk___model___topboard___product_pb2___Product,
)

from app_store_sdk.model.topboard.sprint_pb2 import (
    Sprint as app_store_sdk___model___topboard___sprint_pb2___Sprint,
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


class Issue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class IssueFrom(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        instanceId = ... # type: typing___Text

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            instanceId : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Issue.IssueFrom: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Issue.IssueFrom: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"instanceId",b"instanceId",u"name",b"name"]) -> None: ...

    class Links(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        title = ... # type: typing___Text
        url = ... # type: typing___Text

        def __init__(self,
            *,
            title : typing___Optional[typing___Text] = None,
            url : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Issue.Links: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Issue.Links: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"title",b"title",u"url",b"url"]) -> None: ...

    class Images(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        name = ... # type: typing___Text
        url = ... # type: typing___Text

        def __init__(self,
            *,
            name : typing___Optional[typing___Text] = None,
            url : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Issue.Images: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Issue.Images: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"name",b"name",u"url",b"url"]) -> None: ...

    name = ... # type: typing___Text
    instanceId = ... # type: typing___Text
    creator = ... # type: typing___Text
    ctime = ... # type: typing___Text
    title = ... # type: typing___Text
    description = ... # type: typing___Text
    priority = ... # type: typing___Text
    type = ... # type: typing___Text
    step = ... # type: typing___Text
    storyPoint = ... # type: typing___Text
    resolution = ... # type: typing___Text
    status = ... # type: typing___Text
    bugType = ... # type: typing___Text
    responsibility = ... # type: typing___Text

    @property
    def parent(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Issue]: ...

    @property
    def subtasks(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Issue]: ...

    @property
    def product(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___topboard___product_pb2___Product]: ...

    @property
    def sprint(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___topboard___sprint_pb2___Sprint]: ...

    @property
    def subscribers(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___cmdb___user_pb2___User]: ...

    @property
    def assignee(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___cmdb___user_pb2___User]: ...

    @property
    def reporter(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___cmdb___user_pb2___User]: ...

    @property
    def attachments(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___topboard___attachment_pb2___Attachment]: ...

    @property
    def comments(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___topboard___comment_pb2___Comment]: ...

    @property
    def issueFrom(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Issue.IssueFrom]: ...

    @property
    def tester(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[app_store_sdk___model___cmdb___user_pb2___User]: ...

    @property
    def links(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Issue.Links]: ...

    @property
    def images(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Issue.Images]: ...

    def __init__(self,
        *,
        parent : typing___Optional[typing___Iterable[Issue]] = None,
        subtasks : typing___Optional[typing___Iterable[Issue]] = None,
        product : typing___Optional[typing___Iterable[app_store_sdk___model___topboard___product_pb2___Product]] = None,
        sprint : typing___Optional[typing___Iterable[app_store_sdk___model___topboard___sprint_pb2___Sprint]] = None,
        subscribers : typing___Optional[typing___Iterable[app_store_sdk___model___cmdb___user_pb2___User]] = None,
        assignee : typing___Optional[typing___Iterable[app_store_sdk___model___cmdb___user_pb2___User]] = None,
        reporter : typing___Optional[typing___Iterable[app_store_sdk___model___cmdb___user_pb2___User]] = None,
        attachments : typing___Optional[typing___Iterable[app_store_sdk___model___topboard___attachment_pb2___Attachment]] = None,
        comments : typing___Optional[typing___Iterable[app_store_sdk___model___topboard___comment_pb2___Comment]] = None,
        issueFrom : typing___Optional[typing___Iterable[Issue.IssueFrom]] = None,
        tester : typing___Optional[typing___Iterable[app_store_sdk___model___cmdb___user_pb2___User]] = None,
        name : typing___Optional[typing___Text] = None,
        instanceId : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        ctime : typing___Optional[typing___Text] = None,
        title : typing___Optional[typing___Text] = None,
        description : typing___Optional[typing___Text] = None,
        priority : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        step : typing___Optional[typing___Text] = None,
        links : typing___Optional[typing___Iterable[Issue.Links]] = None,
        storyPoint : typing___Optional[typing___Text] = None,
        resolution : typing___Optional[typing___Text] = None,
        status : typing___Optional[typing___Text] = None,
        images : typing___Optional[typing___Iterable[Issue.Images]] = None,
        bugType : typing___Optional[typing___Text] = None,
        responsibility : typing___Optional[typing___Text] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Issue: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Issue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"assignee",b"assignee",u"attachments",b"attachments",u"bugType",b"bugType",u"comments",b"comments",u"creator",b"creator",u"ctime",b"ctime",u"description",b"description",u"images",b"images",u"instanceId",b"instanceId",u"issueFrom",b"issueFrom",u"links",b"links",u"name",b"name",u"parent",b"parent",u"priority",b"priority",u"product",b"product",u"reporter",b"reporter",u"resolution",b"resolution",u"responsibility",b"responsibility",u"sprint",b"sprint",u"status",b"status",u"step",b"step",u"storyPoint",b"storyPoint",u"subscribers",b"subscribers",u"subtasks",b"subtasks",u"tester",b"tester",u"title",b"title",u"type",b"type"]) -> None: ...
