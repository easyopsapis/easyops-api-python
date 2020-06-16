# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from terraform_sdk.model.container.metadata_pb2 import (
    Metadata as terraform_sdk___model___container___metadata_pb2___Metadata,
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


class NodeDetail(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Spec(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        podCIDR = ... # type: typing___Text
        providerID = ... # type: typing___Text
        unschedulable = ... # type: builtin___bool

        def __init__(self,
            *,
            podCIDR : typing___Optional[typing___Text] = None,
            providerID : typing___Optional[typing___Text] = None,
            unschedulable : typing___Optional[builtin___bool] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> NodeDetail.Spec: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NodeDetail.Spec: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"podCIDR",b"podCIDR",u"providerID",b"providerID",u"unschedulable",b"unschedulable"]) -> None: ...

    class Status(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        class Capacity(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            cpu = ... # type: typing___Text
            memory = ... # type: typing___Text
            pods = ... # type: typing___Text
            ephemeralStorage = ... # type: typing___Text

            def __init__(self,
                *,
                cpu : typing___Optional[typing___Text] = None,
                memory : typing___Optional[typing___Text] = None,
                pods : typing___Optional[typing___Text] = None,
                ephemeralStorage : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> NodeDetail.Status.Capacity: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NodeDetail.Status.Capacity: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"cpu",b"cpu",u"ephemeralStorage",b"ephemeralStorage",u"memory",b"memory",u"pods",b"pods"]) -> None: ...

        class Allocatable(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            cpu = ... # type: typing___Text
            memory = ... # type: typing___Text
            pods = ... # type: typing___Text

            def __init__(self,
                *,
                cpu : typing___Optional[typing___Text] = None,
                memory : typing___Optional[typing___Text] = None,
                pods : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> NodeDetail.Status.Allocatable: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NodeDetail.Status.Allocatable: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"cpu",b"cpu",u"memory",b"memory",u"pods",b"pods"]) -> None: ...

        class NodeInfo(google___protobuf___message___Message):
            DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
            machineID = ... # type: typing___Text
            systemUUID = ... # type: typing___Text
            bootID = ... # type: typing___Text
            kernelVersion = ... # type: typing___Text
            osImage = ... # type: typing___Text
            containerRuntimeVersion = ... # type: typing___Text
            kubeletVersion = ... # type: typing___Text
            kubeProxyVersion = ... # type: typing___Text
            operatingSystem = ... # type: typing___Text
            architecture = ... # type: typing___Text

            def __init__(self,
                *,
                machineID : typing___Optional[typing___Text] = None,
                systemUUID : typing___Optional[typing___Text] = None,
                bootID : typing___Optional[typing___Text] = None,
                kernelVersion : typing___Optional[typing___Text] = None,
                osImage : typing___Optional[typing___Text] = None,
                containerRuntimeVersion : typing___Optional[typing___Text] = None,
                kubeletVersion : typing___Optional[typing___Text] = None,
                kubeProxyVersion : typing___Optional[typing___Text] = None,
                operatingSystem : typing___Optional[typing___Text] = None,
                architecture : typing___Optional[typing___Text] = None,
                ) -> None: ...
            if sys.version_info >= (3,):
                @classmethod
                def FromString(cls, s: builtin___bytes) -> NodeDetail.Status.NodeInfo: ...
            else:
                @classmethod
                def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NodeDetail.Status.NodeInfo: ...
            def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"architecture",b"architecture",u"bootID",b"bootID",u"containerRuntimeVersion",b"containerRuntimeVersion",u"kernelVersion",b"kernelVersion",u"kubeProxyVersion",b"kubeProxyVersion",u"kubeletVersion",b"kubeletVersion",u"machineID",b"machineID",u"operatingSystem",b"operatingSystem",u"osImage",b"osImage",u"systemUUID",b"systemUUID"]) -> None: ...

        phase = ... # type: typing___Text

        @property
        def capacity(self) -> NodeDetail.Status.Capacity: ...

        @property
        def allocatable(self) -> NodeDetail.Status.Allocatable: ...

        @property
        def nodeInfo(self) -> NodeDetail.Status.NodeInfo: ...

        def __init__(self,
            *,
            capacity : typing___Optional[NodeDetail.Status.Capacity] = None,
            allocatable : typing___Optional[NodeDetail.Status.Allocatable] = None,
            phase : typing___Optional[typing___Text] = None,
            nodeInfo : typing___Optional[NodeDetail.Status.NodeInfo] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> NodeDetail.Status: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NodeDetail.Status: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def HasField(self, field_name: typing_extensions___Literal[u"allocatable",b"allocatable",u"capacity",b"capacity",u"nodeInfo",b"nodeInfo"]) -> builtin___bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"allocatable",b"allocatable",u"capacity",b"capacity",u"nodeInfo",b"nodeInfo",u"phase",b"phase"]) -> None: ...

    worker = ... # type: builtin___bool

    @property
    def metadata(self) -> terraform_sdk___model___container___metadata_pb2___Metadata: ...

    @property
    def spec(self) -> NodeDetail.Spec: ...

    @property
    def status(self) -> NodeDetail.Status: ...

    def __init__(self,
        *,
        metadata : typing___Optional[terraform_sdk___model___container___metadata_pb2___Metadata] = None,
        spec : typing___Optional[NodeDetail.Spec] = None,
        status : typing___Optional[NodeDetail.Status] = None,
        worker : typing___Optional[builtin___bool] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> NodeDetail: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> NodeDetail: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"metadata",b"metadata",u"spec",b"spec",u"status",b"status"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"metadata",b"metadata",u"spec",b"spec",u"status",b"status",u"worker",b"worker"]) -> None: ...