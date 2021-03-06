# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='rpcserver',
  syntax='proto3',
  serialized_pb=_b('\n\trpc.proto\x12\trpcserver\"0\n\x06Matrix\x12\x0b\n\x03row\x18\x01 \x01(\x05\x12\x0b\n\x03\x63ol\x18\x02 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x03 \x03(\x01\"b\n\x0e\x43lusterRequest\x12\x15\n\rdim_embedding\x18\x01 \x01(\x05\x12\x12\n\nperplexity\x18\x02 \x01(\x01\x12\x15\n\rlearning_rate\x18\x03 \x01(\x01\x12\x0e\n\x06\x66ields\x18\x04 \x03(\t2F\n\tRPCserver\x12\x39\n\x07\x63luster\x12\x19.rpcserver.ClusterRequest\x1a\x11.rpcserver.Matrix\"\x00\x62\x06proto3')
)




_MATRIX = _descriptor.Descriptor(
  name='Matrix',
  full_name='rpcserver.Matrix',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row', full_name='rpcserver.Matrix.row', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='col', full_name='rpcserver.Matrix.col', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='rpcserver.Matrix.data', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=72,
)


_CLUSTERREQUEST = _descriptor.Descriptor(
  name='ClusterRequest',
  full_name='rpcserver.ClusterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dim_embedding', full_name='rpcserver.ClusterRequest.dim_embedding', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perplexity', full_name='rpcserver.ClusterRequest.perplexity', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='rpcserver.ClusterRequest.learning_rate', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='rpcserver.ClusterRequest.fields', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=172,
)

DESCRIPTOR.message_types_by_name['Matrix'] = _MATRIX
DESCRIPTOR.message_types_by_name['ClusterRequest'] = _CLUSTERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Matrix = _reflection.GeneratedProtocolMessageType('Matrix', (_message.Message,), dict(
  DESCRIPTOR = _MATRIX,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:rpcserver.Matrix)
  ))
_sym_db.RegisterMessage(Matrix)

ClusterRequest = _reflection.GeneratedProtocolMessageType('ClusterRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLUSTERREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:rpcserver.ClusterRequest)
  ))
_sym_db.RegisterMessage(ClusterRequest)



_RPCSERVER = _descriptor.ServiceDescriptor(
  name='RPCserver',
  full_name='rpcserver.RPCserver',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=174,
  serialized_end=244,
  methods=[
  _descriptor.MethodDescriptor(
    name='cluster',
    full_name='rpcserver.RPCserver.cluster',
    index=0,
    containing_service=None,
    input_type=_CLUSTERREQUEST,
    output_type=_MATRIX,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPCSERVER)

DESCRIPTOR.services_by_name['RPCserver'] = _RPCSERVER

# @@protoc_insertion_point(module_scope)
