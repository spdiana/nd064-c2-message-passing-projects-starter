# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: person_kafka_event.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='person_kafka_event.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18person_kafka_event.proto\"L\n\x12PersonEventMessage\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\"\x07\n\x05\x45mpty2p\n\x16PersonEventItemService\x12\x32\n\x06\x43reate\x12\x13.PersonEventMessage\x1a\x13.PersonEventMessage\x12\"\n\x03Get\x12\x06.Empty\x1a\x13.PersonEventMessageb\x06proto3'
)




_PERSONEVENTMESSAGE = _descriptor.Descriptor(
  name='PersonEventMessage',
  full_name='PersonEventMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='PersonEventMessage.person_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='PersonEventMessage.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='PersonEventMessage.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=28,
  serialized_end=104,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=106,
  serialized_end=113,
)

DESCRIPTOR.message_types_by_name['PersonEventMessage'] = _PERSONEVENTMESSAGE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PersonEventMessage = _reflection.GeneratedProtocolMessageType('PersonEventMessage', (_message.Message,), {
  'DESCRIPTOR' : _PERSONEVENTMESSAGE,
  '__module__' : 'person_kafka_event_pb2'
  # @@protoc_insertion_point(class_scope:PersonEventMessage)
  })
_sym_db.RegisterMessage(PersonEventMessage)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'person_kafka_event_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)



_PERSONEVENTITEMSERVICE = _descriptor.ServiceDescriptor(
  name='PersonEventItemService',
  full_name='PersonEventItemService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=115,
  serialized_end=227,
  methods=[
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='PersonEventItemService.Create',
    index=0,
    containing_service=None,
    input_type=_PERSONEVENTMESSAGE,
    output_type=_PERSONEVENTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='PersonEventItemService.Get',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_PERSONEVENTMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PERSONEVENTITEMSERVICE)

DESCRIPTOR.services_by_name['PersonEventItemService'] = _PERSONEVENTITEMSERVICE

# @@protoc_insertion_point(module_scope)
