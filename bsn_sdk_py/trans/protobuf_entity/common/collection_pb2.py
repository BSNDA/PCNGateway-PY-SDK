# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/collection.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import policies_pb2 as common_dot_policies__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/collection.proto',
  package='common',
  syntax='proto3',
  serialized_options=b'\n$org.hyperledger.fabric.protos.commonZ+github.com/hyperledger/fabric/protos/common',
  serialized_pb=b'\n\x17\x63ommon/collection.proto\x12\x06\x63ommon\x1a\x15\x63ommon/policies.proto\"C\n\x17\x43ollectionConfigPackage\x12(\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\x18.common.CollectionConfig\"a\n\x10\x43ollectionConfig\x12\x42\n\x18static_collection_config\x18\x01 \x01(\x0b\x32\x1e.common.StaticCollectionConfigH\x00\x42\t\n\x07payload\"\xcc\x01\n\x16StaticCollectionConfig\x12\x0c\n\x04name\x18\x01 \x01(\t\x12:\n\x12member_orgs_policy\x18\x02 \x01(\x0b\x32\x1e.common.CollectionPolicyConfig\x12\x1b\n\x13required_peer_count\x18\x03 \x01(\x05\x12\x1a\n\x12maximum_peer_count\x18\x04 \x01(\x05\x12\x15\n\rblock_to_live\x18\x05 \x01(\x04\x12\x18\n\x10member_only_read\x18\x06 \x01(\x08\"`\n\x16\x43ollectionPolicyConfig\x12;\n\x10signature_policy\x18\x01 \x01(\x0b\x32\x1f.common.SignaturePolicyEnvelopeH\x00\x42\t\n\x07payload\"[\n\x12\x43ollectionCriteria\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\t\x12\r\n\x05tx_id\x18\x02 \x01(\t\x12\x12\n\ncollection\x18\x03 \x01(\t\x12\x11\n\tnamespace\x18\x04 \x01(\tBS\n$org.hyperledger.fabric.protos.commonZ+github.com/hyperledger/fabric/protos/commonb\x06proto3'
  ,
  dependencies=[common_dot_policies__pb2.DESCRIPTOR,])




_COLLECTIONCONFIGPACKAGE = _descriptor.Descriptor(
  name='CollectionConfigPackage',
  full_name='common.CollectionConfigPackage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='config', full_name='common.CollectionConfigPackage.config', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=58,
  serialized_end=125,
)


_COLLECTIONCONFIG = _descriptor.Descriptor(
  name='CollectionConfig',
  full_name='common.CollectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='static_collection_config', full_name='common.CollectionConfig.static_collection_config', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='common.CollectionConfig.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=127,
  serialized_end=224,
)


_STATICCOLLECTIONCONFIG = _descriptor.Descriptor(
  name='StaticCollectionConfig',
  full_name='common.StaticCollectionConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='common.StaticCollectionConfig.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_orgs_policy', full_name='common.StaticCollectionConfig.member_orgs_policy', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='required_peer_count', full_name='common.StaticCollectionConfig.required_peer_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maximum_peer_count', full_name='common.StaticCollectionConfig.maximum_peer_count', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_to_live', full_name='common.StaticCollectionConfig.block_to_live', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_only_read', full_name='common.StaticCollectionConfig.member_only_read', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=227,
  serialized_end=431,
)


_COLLECTIONPOLICYCONFIG = _descriptor.Descriptor(
  name='CollectionPolicyConfig',
  full_name='common.CollectionPolicyConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_policy', full_name='common.CollectionPolicyConfig.signature_policy', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='common.CollectionPolicyConfig.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=433,
  serialized_end=529,
)


_COLLECTIONCRITERIA = _descriptor.Descriptor(
  name='CollectionCriteria',
  full_name='common.CollectionCriteria',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='common.CollectionCriteria.channel', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_id', full_name='common.CollectionCriteria.tx_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection', full_name='common.CollectionCriteria.collection', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='namespace', full_name='common.CollectionCriteria.namespace', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=531,
  serialized_end=622,
)

_COLLECTIONCONFIGPACKAGE.fields_by_name['config'].message_type = _COLLECTIONCONFIG
_COLLECTIONCONFIG.fields_by_name['static_collection_config'].message_type = _STATICCOLLECTIONCONFIG
_COLLECTIONCONFIG.oneofs_by_name['payload'].fields.append(
  _COLLECTIONCONFIG.fields_by_name['static_collection_config'])
_COLLECTIONCONFIG.fields_by_name['static_collection_config'].containing_oneof = _COLLECTIONCONFIG.oneofs_by_name['payload']
_STATICCOLLECTIONCONFIG.fields_by_name['member_orgs_policy'].message_type = _COLLECTIONPOLICYCONFIG
_COLLECTIONPOLICYCONFIG.fields_by_name['signature_policy'].message_type = common_dot_policies__pb2._SIGNATUREPOLICYENVELOPE
_COLLECTIONPOLICYCONFIG.oneofs_by_name['payload'].fields.append(
  _COLLECTIONPOLICYCONFIG.fields_by_name['signature_policy'])
_COLLECTIONPOLICYCONFIG.fields_by_name['signature_policy'].containing_oneof = _COLLECTIONPOLICYCONFIG.oneofs_by_name['payload']
DESCRIPTOR.message_types_by_name['CollectionConfigPackage'] = _COLLECTIONCONFIGPACKAGE
DESCRIPTOR.message_types_by_name['CollectionConfig'] = _COLLECTIONCONFIG
DESCRIPTOR.message_types_by_name['StaticCollectionConfig'] = _STATICCOLLECTIONCONFIG
DESCRIPTOR.message_types_by_name['CollectionPolicyConfig'] = _COLLECTIONPOLICYCONFIG
DESCRIPTOR.message_types_by_name['CollectionCriteria'] = _COLLECTIONCRITERIA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectionConfigPackage = _reflection.GeneratedProtocolMessageType('CollectionConfigPackage', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONCONFIGPACKAGE,
  '__module__' : 'common.collection_pb2'
  # @@protoc_insertion_point(class_scope:common.CollectionConfigPackage)
  })
_sym_db.RegisterMessage(CollectionConfigPackage)

CollectionConfig = _reflection.GeneratedProtocolMessageType('CollectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONCONFIG,
  '__module__' : 'common.collection_pb2'
  # @@protoc_insertion_point(class_scope:common.CollectionConfig)
  })
_sym_db.RegisterMessage(CollectionConfig)

StaticCollectionConfig = _reflection.GeneratedProtocolMessageType('StaticCollectionConfig', (_message.Message,), {
  'DESCRIPTOR' : _STATICCOLLECTIONCONFIG,
  '__module__' : 'common.collection_pb2'
  # @@protoc_insertion_point(class_scope:common.StaticCollectionConfig)
  })
_sym_db.RegisterMessage(StaticCollectionConfig)

CollectionPolicyConfig = _reflection.GeneratedProtocolMessageType('CollectionPolicyConfig', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONPOLICYCONFIG,
  '__module__' : 'common.collection_pb2'
  # @@protoc_insertion_point(class_scope:common.CollectionPolicyConfig)
  })
_sym_db.RegisterMessage(CollectionPolicyConfig)

CollectionCriteria = _reflection.GeneratedProtocolMessageType('CollectionCriteria', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONCRITERIA,
  '__module__' : 'common.collection_pb2'
  # @@protoc_insertion_point(class_scope:common.CollectionCriteria)
  })
_sym_db.RegisterMessage(CollectionCriteria)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
