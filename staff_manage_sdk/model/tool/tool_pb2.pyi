# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.struct_pb2 import (
    Value as google___protobuf___struct_pb2___Value,
)

from staff_manage_sdk.model.tool.tool_input_pb2 import (
    ToolInput as staff_manage_sdk___model___tool___tool_input_pb2___ToolInput,
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


class Tool(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class OutputDefs(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        id = ... # type: typing___Text
        name = ... # type: typing___Text

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Tool.OutputDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Tool.OutputDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

    class TableDefs(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Dimensions(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            id = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> Tool.TableDefs.Dimensions: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Tool.TableDefs.Dimensions: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

        class Columns(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            id = ... # type: typing___Text
            name = ... # type: typing___Text

            def __init__(self,
                *,
                id : typing___Optional[typing___Text] = None,
                name : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> Tool.TableDefs.Columns: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Tool.TableDefs.Columns: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"id",b"id",u"name",b"name"]) -> None: ...

        id = ... # type: typing___Text
        name = ... # type: typing___Text

        @property
        def dimensions(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Tool.TableDefs.Dimensions]: ...

        @property
        def columns(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Tool.TableDefs.Columns]: ...

        def __init__(self,
            *,
            id : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            dimensions : typing___Optional[typing___Iterable[Tool.TableDefs.Dimensions]] = None,
            columns : typing___Optional[typing___Iterable[Tool.TableDefs.Columns]] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Tool.TableDefs: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Tool.TableDefs: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"columns",b"columns",u"dimensions",b"dimensions",u"id",b"id",u"name",b"name"]) -> None: ...

    class Log(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        enabled = ... # type: builtin___bool
        level = ... # type: typing___Text

        def __init__(self,
            *,
            enabled : typing___Optional[builtin___bool] = None,
            level : typing___Optional[typing___Text] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> Tool.Log: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Tool.Log: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"enabled",b"enabled",u"level",b"level"]) -> None: ...

    toolId = ... # type: typing___Text
    vId = ... # type: typing___Text
    name = ... # type: typing___Text
    timeout = ... # type: builtin___int
    category = ... # type: typing___Text
    icon = ... # type: typing___Text
    style = ... # type: typing___Text
    memo = ... # type: typing___Text
    listVisible = ... # type: builtin___bool
    tags = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    disable = ... # type: builtin___bool
    createTime = ... # type: typing___Text
    updateTime = ... # type: typing___Text
    creator = ... # type: typing___Text
    org = ... # type: builtin___int
    outputs = ... # type: typing___Text
    type = ... # type: typing___Text
    content = ... # type: typing___Text
    defaultExecUser = ... # type: typing___Text
    execUser = ... # type: typing___Text
    authUsers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    defaultAgents = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    system_plugin = ... # type: builtin___bool
    system_tool = ... # type: builtin___bool
    lockAgents = ... # type: typing___Text
    sandboxRun = ... # type: builtin___bool
    whiteList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    windowsSession = ... # type: builtin___bool
    blackList = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    vCreateTime = ... # type: typing___Text
    vUpdateTime = ... # type: typing___Text
    vName = ... # type: typing___Text
    vCreator = ... # type: typing___Text
    readAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    updateAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    deleteAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    executeAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    readExecutionResultAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    rootExecuteAuthorizers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    vDesc = ... # type: typing___Text
    sourceFrom = ... # type: typing___Text
    envType = ... # type: typing___Text
    checkType = ... # type: typing___Text
    checkUser = ... # type: typing___Text
    checkSponsor = ... # type: typing___Text
    checkComment = ... # type: typing___Text
    functionType = ... # type: typing___Text
    is_system_org = ... # type: builtin___bool
    subscribers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    subscribedChannel = ... # type: typing___Text
    readOnly = ... # type: builtin___bool
    templateType = ... # type: typing___Text
    delete_me = ... # type: builtin___bool
    approvers = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text]
    ansibleNodeExecUser = ... # type: typing___Text

    @property
    def inputs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[staff_manage_sdk___model___tool___tool_input_pb2___ToolInput]: ...

    @property
    def toolOutputs(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def outputDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Tool.OutputDefs]: ...

    @property
    def tableDefs(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[Tool.TableDefs]: ...

    @property
    def batchStrategy(self) -> google___protobuf___struct_pb2___Value: ...

    @property
    def log(self) -> Tool.Log: ...

    def __init__(self,
        *,
        toolId : typing___Optional[typing___Text] = None,
        vId : typing___Optional[typing___Text] = None,
        name : typing___Optional[typing___Text] = None,
        timeout : typing___Optional[builtin___int] = None,
        category : typing___Optional[typing___Text] = None,
        icon : typing___Optional[typing___Text] = None,
        style : typing___Optional[typing___Text] = None,
        memo : typing___Optional[typing___Text] = None,
        listVisible : typing___Optional[builtin___bool] = None,
        tags : typing___Optional[typing___Iterable[typing___Text]] = None,
        disable : typing___Optional[builtin___bool] = None,
        createTime : typing___Optional[typing___Text] = None,
        updateTime : typing___Optional[typing___Text] = None,
        creator : typing___Optional[typing___Text] = None,
        org : typing___Optional[builtin___int] = None,
        inputs : typing___Optional[typing___Iterable[staff_manage_sdk___model___tool___tool_input_pb2___ToolInput]] = None,
        outputs : typing___Optional[typing___Text] = None,
        type : typing___Optional[typing___Text] = None,
        content : typing___Optional[typing___Text] = None,
        defaultExecUser : typing___Optional[typing___Text] = None,
        execUser : typing___Optional[typing___Text] = None,
        authUsers : typing___Optional[typing___Iterable[typing___Text]] = None,
        defaultAgents : typing___Optional[typing___Iterable[typing___Text]] = None,
        system_plugin : typing___Optional[builtin___bool] = None,
        system_tool : typing___Optional[builtin___bool] = None,
        lockAgents : typing___Optional[typing___Text] = None,
        sandboxRun : typing___Optional[builtin___bool] = None,
        whiteList : typing___Optional[typing___Iterable[typing___Text]] = None,
        windowsSession : typing___Optional[builtin___bool] = None,
        blackList : typing___Optional[typing___Iterable[typing___Text]] = None,
        toolOutputs : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        outputDefs : typing___Optional[typing___Iterable[Tool.OutputDefs]] = None,
        tableDefs : typing___Optional[typing___Iterable[Tool.TableDefs]] = None,
        vCreateTime : typing___Optional[typing___Text] = None,
        vUpdateTime : typing___Optional[typing___Text] = None,
        vName : typing___Optional[typing___Text] = None,
        vCreator : typing___Optional[typing___Text] = None,
        readAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        updateAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        deleteAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        executeAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        readExecutionResultAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        rootExecuteAuthorizers : typing___Optional[typing___Iterable[typing___Text]] = None,
        vDesc : typing___Optional[typing___Text] = None,
        sourceFrom : typing___Optional[typing___Text] = None,
        envType : typing___Optional[typing___Text] = None,
        checkType : typing___Optional[typing___Text] = None,
        checkUser : typing___Optional[typing___Text] = None,
        checkSponsor : typing___Optional[typing___Text] = None,
        checkComment : typing___Optional[typing___Text] = None,
        batchStrategy : typing___Optional[google___protobuf___struct_pb2___Value] = None,
        functionType : typing___Optional[typing___Text] = None,
        is_system_org : typing___Optional[builtin___bool] = None,
        subscribers : typing___Optional[typing___Iterable[typing___Text]] = None,
        subscribedChannel : typing___Optional[typing___Text] = None,
        readOnly : typing___Optional[builtin___bool] = None,
        templateType : typing___Optional[typing___Text] = None,
        delete_me : typing___Optional[builtin___bool] = None,
        approvers : typing___Optional[typing___Iterable[typing___Text]] = None,
        ansibleNodeExecUser : typing___Optional[typing___Text] = None,
        log : typing___Optional[Tool.Log] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> Tool: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> Tool: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"batchStrategy",b"batchStrategy",u"log",b"log",u"toolOutputs",b"toolOutputs"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"ansibleNodeExecUser",b"ansibleNodeExecUser",u"approvers",b"approvers",u"authUsers",b"authUsers",u"batchStrategy",b"batchStrategy",u"blackList",b"blackList",u"category",b"category",u"checkComment",b"checkComment",u"checkSponsor",b"checkSponsor",u"checkType",b"checkType",u"checkUser",b"checkUser",u"content",b"content",u"createTime",b"createTime",u"creator",b"creator",u"defaultAgents",b"defaultAgents",u"defaultExecUser",b"defaultExecUser",u"deleteAuthorizers",b"deleteAuthorizers",u"delete_me",b"delete_me",u"disable",b"disable",u"envType",b"envType",u"execUser",b"execUser",u"executeAuthorizers",b"executeAuthorizers",u"functionType",b"functionType",u"icon",b"icon",u"inputs",b"inputs",u"is_system_org",b"is_system_org",u"listVisible",b"listVisible",u"lockAgents",b"lockAgents",u"log",b"log",u"memo",b"memo",u"name",b"name",u"org",b"org",u"outputDefs",b"outputDefs",u"outputs",b"outputs",u"readAuthorizers",b"readAuthorizers",u"readExecutionResultAuthorizers",b"readExecutionResultAuthorizers",u"readOnly",b"readOnly",u"rootExecuteAuthorizers",b"rootExecuteAuthorizers",u"sandboxRun",b"sandboxRun",u"sourceFrom",b"sourceFrom",u"style",b"style",u"subscribedChannel",b"subscribedChannel",u"subscribers",b"subscribers",u"system_plugin",b"system_plugin",u"system_tool",b"system_tool",u"tableDefs",b"tableDefs",u"tags",b"tags",u"templateType",b"templateType",u"timeout",b"timeout",u"toolId",b"toolId",u"toolOutputs",b"toolOutputs",u"type",b"type",u"updateAuthorizers",b"updateAuthorizers",u"updateTime",b"updateTime",u"vCreateTime",b"vCreateTime",u"vCreator",b"vCreator",u"vDesc",b"vDesc",u"vId",b"vId",u"vName",b"vName",u"vUpdateTime",b"vUpdateTime",u"whiteList",b"whiteList",u"windowsSession",b"windowsSession"]) -> None: ...
