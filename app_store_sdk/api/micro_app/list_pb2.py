# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: list.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from model.app_store import app_version_pb2 as model_dot_app__store_dot_app__version__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='list.proto',
  package='micro_app',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nlist.proto\x12\tmicro_app\x1a!model/app_store/app_version.proto\"\xef\x01\n\x1bListAppStoreMicroAppRequest\x12\x0c\n\x04page\x18\x01 \x01(\x05\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12;\n\x05query\x18\x03 \x01(\x0b\x32,.micro_app.ListAppStoreMicroAppRequest.Query\x12\x39\n\x04sort\x18\x04 \x01(\x0b\x32+.micro_app.ListAppStoreMicroAppRequest.Sort\x1a!\n\x05Query\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x03(\t\x1a\x14\n\x04Sort\x12\x0c\n\x04name\x18\x01 \x01(\x05\"\x9f\x02\n\x1cListAppStoreMicroAppResponse\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12:\n\x04list\x18\x04 \x03(\x0b\x32,.micro_app.ListAppStoreMicroAppResponse.List\x1a\x92\x01\n\x04List\x12-\n\x0e\x63urrentVersion\x18\x01 \x01(\x0b\x32\x15.app_store.AppVersion\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\n\n\x02id\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x04 \x01(\t\x12\r\n\x05intro\x18\x05 \x01(\t\x12\x0f\n\x07preview\x18\x06 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\"\x8e\x01\n#ListAppStoreMicroAppResponseWrapper\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x13\n\x0b\x63odeExplain\x18\x02 \x01(\t\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x35\n\x04\x64\x61ta\x18\x04 \x01(\x0b\x32\'.micro_app.ListAppStoreMicroAppResponseb\x06proto3')
  ,
  dependencies=[model_dot_app__store_dot_app__version__pb2.DESCRIPTOR,])




_LISTAPPSTOREMICROAPPREQUEST_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='micro_app.ListAppStoreMicroAppRequest.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.ListAppStoreMicroAppRequest.Query.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='micro_app.ListAppStoreMicroAppRequest.Query.id', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=245,
  serialized_end=278,
)

_LISTAPPSTOREMICROAPPREQUEST_SORT = _descriptor.Descriptor(
  name='Sort',
  full_name='micro_app.ListAppStoreMicroAppRequest.Sort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.ListAppStoreMicroAppRequest.Sort.name', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=300,
)

_LISTAPPSTOREMICROAPPREQUEST = _descriptor.Descriptor(
  name='ListAppStoreMicroAppRequest',
  full_name='micro_app.ListAppStoreMicroAppRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='page', full_name='micro_app.ListAppStoreMicroAppRequest.page', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='micro_app.ListAppStoreMicroAppRequest.page_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='query', full_name='micro_app.ListAppStoreMicroAppRequest.query', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sort', full_name='micro_app.ListAppStoreMicroAppRequest.sort', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTAPPSTOREMICROAPPREQUEST_QUERY, _LISTAPPSTOREMICROAPPREQUEST_SORT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=300,
)


_LISTAPPSTOREMICROAPPRESPONSE_LIST = _descriptor.Descriptor(
  name='List',
  full_name='micro_app.ListAppStoreMicroAppResponse.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currentVersion', full_name='micro_app.ListAppStoreMicroAppResponse.List.currentVersion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='micro_app.ListAppStoreMicroAppResponse.List.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='micro_app.ListAppStoreMicroAppResponse.List.id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='micro_app.ListAppStoreMicroAppResponse.List.icon', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intro', full_name='micro_app.ListAppStoreMicroAppResponse.List.intro', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preview', full_name='micro_app.ListAppStoreMicroAppResponse.List.preview', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='micro_app.ListAppStoreMicroAppResponse.List.description', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=444,
  serialized_end=590,
)

_LISTAPPSTOREMICROAPPRESPONSE = _descriptor.Descriptor(
  name='ListAppStoreMicroAppResponse',
  full_name='micro_app.ListAppStoreMicroAppResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='micro_app.ListAppStoreMicroAppResponse.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='micro_app.ListAppStoreMicroAppResponse.page', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='micro_app.ListAppStoreMicroAppResponse.page_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list', full_name='micro_app.ListAppStoreMicroAppResponse.list', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_LISTAPPSTOREMICROAPPRESPONSE_LIST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=590,
)


_LISTAPPSTOREMICROAPPRESPONSEWRAPPER = _descriptor.Descriptor(
  name='ListAppStoreMicroAppResponseWrapper',
  full_name='micro_app.ListAppStoreMicroAppResponseWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='micro_app.ListAppStoreMicroAppResponseWrapper.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='codeExplain', full_name='micro_app.ListAppStoreMicroAppResponseWrapper.codeExplain', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='micro_app.ListAppStoreMicroAppResponseWrapper.error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='micro_app.ListAppStoreMicroAppResponseWrapper.data', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=593,
  serialized_end=735,
)

_LISTAPPSTOREMICROAPPREQUEST_QUERY.containing_type = _LISTAPPSTOREMICROAPPREQUEST
_LISTAPPSTOREMICROAPPREQUEST_SORT.containing_type = _LISTAPPSTOREMICROAPPREQUEST
_LISTAPPSTOREMICROAPPREQUEST.fields_by_name['query'].message_type = _LISTAPPSTOREMICROAPPREQUEST_QUERY
_LISTAPPSTOREMICROAPPREQUEST.fields_by_name['sort'].message_type = _LISTAPPSTOREMICROAPPREQUEST_SORT
_LISTAPPSTOREMICROAPPRESPONSE_LIST.fields_by_name['currentVersion'].message_type = model_dot_app__store_dot_app__version__pb2._APPVERSION
_LISTAPPSTOREMICROAPPRESPONSE_LIST.containing_type = _LISTAPPSTOREMICROAPPRESPONSE
_LISTAPPSTOREMICROAPPRESPONSE.fields_by_name['list'].message_type = _LISTAPPSTOREMICROAPPRESPONSE_LIST
_LISTAPPSTOREMICROAPPRESPONSEWRAPPER.fields_by_name['data'].message_type = _LISTAPPSTOREMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['ListAppStoreMicroAppRequest'] = _LISTAPPSTOREMICROAPPREQUEST
DESCRIPTOR.message_types_by_name['ListAppStoreMicroAppResponse'] = _LISTAPPSTOREMICROAPPRESPONSE
DESCRIPTOR.message_types_by_name['ListAppStoreMicroAppResponseWrapper'] = _LISTAPPSTOREMICROAPPRESPONSEWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAppStoreMicroAppRequest = _reflection.GeneratedProtocolMessageType('ListAppStoreMicroAppRequest', (_message.Message,), dict(

  Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
    DESCRIPTOR = _LISTAPPSTOREMICROAPPREQUEST_QUERY,
    __module__ = 'list_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.ListAppStoreMicroAppRequest.Query)
    ))
  ,

  Sort = _reflection.GeneratedProtocolMessageType('Sort', (_message.Message,), dict(
    DESCRIPTOR = _LISTAPPSTOREMICROAPPREQUEST_SORT,
    __module__ = 'list_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.ListAppStoreMicroAppRequest.Sort)
    ))
  ,
  DESCRIPTOR = _LISTAPPSTOREMICROAPPREQUEST,
  __module__ = 'list_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.ListAppStoreMicroAppRequest)
  ))
_sym_db.RegisterMessage(ListAppStoreMicroAppRequest)
_sym_db.RegisterMessage(ListAppStoreMicroAppRequest.Query)
_sym_db.RegisterMessage(ListAppStoreMicroAppRequest.Sort)

ListAppStoreMicroAppResponse = _reflection.GeneratedProtocolMessageType('ListAppStoreMicroAppResponse', (_message.Message,), dict(

  List = _reflection.GeneratedProtocolMessageType('List', (_message.Message,), dict(
    DESCRIPTOR = _LISTAPPSTOREMICROAPPRESPONSE_LIST,
    __module__ = 'list_pb2'
    # @@protoc_insertion_point(class_scope:micro_app.ListAppStoreMicroAppResponse.List)
    ))
  ,
  DESCRIPTOR = _LISTAPPSTOREMICROAPPRESPONSE,
  __module__ = 'list_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.ListAppStoreMicroAppResponse)
  ))
_sym_db.RegisterMessage(ListAppStoreMicroAppResponse)
_sym_db.RegisterMessage(ListAppStoreMicroAppResponse.List)

ListAppStoreMicroAppResponseWrapper = _reflection.GeneratedProtocolMessageType('ListAppStoreMicroAppResponseWrapper', (_message.Message,), dict(
  DESCRIPTOR = _LISTAPPSTOREMICROAPPRESPONSEWRAPPER,
  __module__ = 'list_pb2'
  # @@protoc_insertion_point(class_scope:micro_app.ListAppStoreMicroAppResponseWrapper)
  ))
_sym_db.RegisterMessage(ListAppStoreMicroAppResponseWrapper)


# @@protoc_insertion_point(module_scope)
