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


class GetIDCRackExcelRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class Data(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        idcName = ... # type: typing___Text
        status = ... # type: typing___Text
        type = ... # type: typing___Text
        occupiedU = ... # type: builtin___int
        occupiedUPercentage = ... # type: typing___Text
        maxuSize = ... # type: builtin___int
        products = ... # type: typing___Text
        customers = ... # type: typing___Text
        hasSinglePowerDevice = ... # type: builtin___bool
        memo = ... # type: typing___Text
        instanceId = ... # type: typing___Text
        name = ... # type: typing___Text
        code = ... # type: typing___Text
        unum = ... # type: builtin___int
        freeUnum = ... # type: builtin___int

        def __init__(self,
            *,
            idcName : typing___Optional[typing___Text] = None,
            status : typing___Optional[typing___Text] = None,
            type : typing___Optional[typing___Text] = None,
            occupiedU : typing___Optional[builtin___int] = None,
            occupiedUPercentage : typing___Optional[typing___Text] = None,
            maxuSize : typing___Optional[builtin___int] = None,
            products : typing___Optional[typing___Text] = None,
            customers : typing___Optional[typing___Text] = None,
            hasSinglePowerDevice : typing___Optional[builtin___bool] = None,
            memo : typing___Optional[typing___Text] = None,
            instanceId : typing___Optional[typing___Text] = None,
            name : typing___Optional[typing___Text] = None,
            code : typing___Optional[typing___Text] = None,
            unum : typing___Optional[builtin___int] = None,
            freeUnum : typing___Optional[builtin___int] = None,
            ) -> None: ...
        if sys.version_info >= (3,):
            @classmethod
            def FromString(cls, s: builtin___bytes) -> GetIDCRackExcelRequest.Data: ...
        else:
            @classmethod
            def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetIDCRackExcelRequest.Data: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"code",b"code",u"customers",b"customers",u"freeUnum",b"freeUnum",u"hasSinglePowerDevice",b"hasSinglePowerDevice",u"idcName",b"idcName",u"instanceId",b"instanceId",u"maxuSize",b"maxuSize",u"memo",b"memo",u"name",b"name",u"occupiedU",b"occupiedU",u"occupiedUPercentage",b"occupiedUPercentage",u"products",b"products",u"status",b"status",u"type",b"type",u"unum",b"unum"]) -> None: ...

    idcId = ... # type: typing___Text
    fileName = ... # type: typing___Text

    @property
    def data(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[GetIDCRackExcelRequest.Data]: ...

    def __init__(self,
        *,
        idcId : typing___Optional[typing___Text] = None,
        fileName : typing___Optional[typing___Text] = None,
        data : typing___Optional[typing___Iterable[GetIDCRackExcelRequest.Data]] = None,
        ) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> GetIDCRackExcelRequest: ...
    else:
        @classmethod
        def FromString(cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]) -> GetIDCRackExcelRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"data",b"data",u"fileName",b"fileName",u"idcId",b"idcId"]) -> None: ...
