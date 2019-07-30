# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Struct as google___protobuf___struct_pb2___Struct,
)

from model.pipeline.build_status_pb2 import (
    BuildStatus as model___pipeline___build_status_pb2___BuildStatus,
)

from model.pipeline.git_meta_pb2 import (
    GitMeta as model___pipeline___git_meta_pb2___GitMeta,
)

from model.pipeline.pipeline_pb2 import (
    Pipeline as model___pipeline___pipeline_pb2___Pipeline,
)

from model.pipeline.project_pb2 import (
    Project as model___pipeline___project_pb2___Project,
)

from model.pipeline.stage_status_pb2 import (
    StageStatus as model___pipeline___stage_status_pb2___StageStatus,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class ListRequest(google___protobuf___message___Message):
    page = ... # type: int
    page_size = ... # type: int

    @property
    def query(self) -> google___protobuf___struct_pb2___Struct: ...

    @property
    def sort(self) -> google___protobuf___struct_pb2___Struct: ...

    def __init__(self,
        page : typing___Optional[int] = None,
        page_size : typing___Optional[int] = None,
        query : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        sort : typing___Optional[google___protobuf___struct_pb2___Struct] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"query",u"sort"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"page",u"page_size",u"query",u"sort"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"query",b"query",u"sort",b"sort"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"page",b"page_size",b"query",b"sort"]) -> None: ...

class ListResponse(google___protobuf___message___Message):
    class Data(google___protobuf___message___Message):
        class List(google___protobuf___message___Message):
            id = ... # type: typing___Text
            sender = ... # type: typing___Text
            created = ... # type: int
            yaml_string = ... # type: typing___Text
            number = ... # type: typing___Text

            @property
            def project(self) -> model___pipeline___project_pb2___Project: ...

            @property
            def pipeline(self) -> model___pipeline___pipeline_pb2___Pipeline: ...

            @property
            def stages(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[model___pipeline___stage_status_pb2___StageStatus]: ...

            @property
            def git_meta(self) -> model___pipeline___git_meta_pb2___GitMeta: ...

            @property
            def status(self) -> model___pipeline___build_status_pb2___BuildStatus: ...

            def __init__(self,
                project : typing___Optional[model___pipeline___project_pb2___Project] = None,
                pipeline : typing___Optional[model___pipeline___pipeline_pb2___Pipeline] = None,
                stages : typing___Optional[typing___Iterable[model___pipeline___stage_status_pb2___StageStatus]] = None,
                id : typing___Optional[typing___Text] = None,
                git_meta : typing___Optional[model___pipeline___git_meta_pb2___GitMeta] = None,
                sender : typing___Optional[typing___Text] = None,
                created : typing___Optional[int] = None,
                yaml_string : typing___Optional[typing___Text] = None,
                status : typing___Optional[model___pipeline___build_status_pb2___BuildStatus] = None,
                number : typing___Optional[typing___Text] = None,
                ) -> None: ...
            @classmethod
            def FromString(cls, s: bytes) -> ListResponse.Data.List: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            if sys.version_info >= (3,):
                def HasField(self, field_name: typing_extensions___Literal[u"git_meta",u"pipeline",u"project",u"status"]) -> bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[u"created",u"git_meta",u"id",u"number",u"pipeline",u"project",u"sender",u"stages",u"status",u"yaml_string"]) -> None: ...
            else:
                def HasField(self, field_name: typing_extensions___Literal[u"git_meta",b"git_meta",u"pipeline",b"pipeline",u"project",b"project",u"status",b"status"]) -> bool: ...
                def ClearField(self, field_name: typing_extensions___Literal[b"created",b"git_meta",b"id",b"number",b"pipeline",b"project",b"sender",b"stages",b"status",b"yaml_string"]) -> None: ...

        total = ... # type: int
        page = ... # type: int
        page_size = ... # type: int

        @property
        def list(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ListResponse.Data.List]: ...

        def __init__(self,
            total : typing___Optional[int] = None,
            page : typing___Optional[int] = None,
            page_size : typing___Optional[int] = None,
            list : typing___Optional[typing___Iterable[ListResponse.Data.List]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> ListResponse.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"list",u"page",u"page_size",u"total"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[b"list",b"page",b"page_size",b"total"]) -> None: ...

    code = ... # type: int
    error = ... # type: typing___Text
    message = ... # type: typing___Text

    @property
    def data(self) -> ListResponse.Data: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        error : typing___Optional[typing___Text] = None,
        message : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListResponse.Data] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"data",u"error",u"message"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"data",b"error",b"message"]) -> None: ...

class ListResponseWrapper(google___protobuf___message___Message):
    code = ... # type: int
    codeExplain = ... # type: typing___Text
    error = ... # type: typing___Text

    @property
    def data(self) -> ListResponse: ...

    def __init__(self,
        code : typing___Optional[int] = None,
        codeExplain : typing___Optional[typing___Text] = None,
        error : typing___Optional[typing___Text] = None,
        data : typing___Optional[ListResponse] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ListResponseWrapper: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",u"codeExplain",u"data",u"error"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"data",b"data"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[b"code",b"codeExplain",b"data",b"error"]) -> None: ...
