# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/Arrow.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/Arrow.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bstreamlit/proto/Arrow.proto\".\n\x05\x41rrow\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x17\n\x06styler\x18\x02 \x01(\x0b\x32\x07.Styler\"O\n\x06Styler\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61ption\x18\x02 \x01(\t\x12\x0e\n\x06styles\x18\x03 \x01(\t\x12\x16\n\x0e\x64isplay_values\x18\x04 \x01(\x0c\x62\x06proto3'
)




_ARROW = _descriptor.Descriptor(
  name='Arrow',
  full_name='Arrow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='Arrow.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='styler', full_name='Arrow.styler', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=31,
  serialized_end=77,
)


_STYLER = _descriptor.Descriptor(
  name='Styler',
  full_name='Styler',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='Styler.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='caption', full_name='Styler.caption', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='styles', full_name='Styler.styles', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='display_values', full_name='Styler.display_values', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=79,
  serialized_end=158,
)

_ARROW.fields_by_name['styler'].message_type = _STYLER
DESCRIPTOR.message_types_by_name['Arrow'] = _ARROW
DESCRIPTOR.message_types_by_name['Styler'] = _STYLER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Arrow = _reflection.GeneratedProtocolMessageType('Arrow', (_message.Message,), {
  'DESCRIPTOR' : _ARROW,
  '__module__' : 'streamlit.proto.Arrow_pb2'
  # @@protoc_insertion_point(class_scope:Arrow)
  })
_sym_db.RegisterMessage(Arrow)

Styler = _reflection.GeneratedProtocolMessageType('Styler', (_message.Message,), {
  'DESCRIPTOR' : _STYLER,
  '__module__' : 'streamlit.proto.Arrow_pb2'
  # @@protoc_insertion_point(class_scope:Styler)
  })
_sym_db.RegisterMessage(Styler)


# @@protoc_insertion_point(module_scope)
