# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tradingrpc.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tradingrpc.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10tradingrpc.proto\x1a\x19google/protobuf/any.proto\"e\n\x0c\x44\x61taResponse\x12\x12\n\nStatusCode\x18\x01 \x01(\x05\x12\"\n\x04\x44\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0b\n\x03Msg\x18\x03 \x01(\t\x12\x10\n\x08\x45rrorMsg\x18\x04 \x01(\t\"\\\n\tEmptyData\x12\"\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32\x14.EmptyData.DataEntry\x1a+\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"r\n\x0b\x44\x61taRequest\x12\x30\n\nParameters\x18\x01 \x03(\x0b\x32\x1c.DataRequest.ParametersEntry\x1a\x31\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x86\x01\n\x05Kline\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\n\n\x02Ts\x18\x02 \x01(\x03\x12\x0c\n\x04Open\x18\x03 \x01(\x02\x12\r\n\x05\x43lose\x18\x04 \x01(\x02\x12\x0c\n\x04High\x18\x05 \x01(\x02\x12\x0b\n\x03Low\x18\x06 \x01(\x02\x12\x0e\n\x06\x41mount\x18\x07 \x01(\x02\x12\r\n\x05\x43ount\x18\x08 \x01(\x02\x12\x0e\n\x06Volume\x18\t \x01(\x02\".\n\x06Klines\x12\x0e\n\x06Result\x18\x01 \x01(\x08\x12\x14\n\x04\x44\x61ta\x18\x02 \x03(\x0b\x32\x06.Kline\"S\n\x07History\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\n\n\x02Ts\x18\x02 \x01(\x03\x12\r\n\x05Price\x18\x03 \x01(\x02\x12\x0e\n\x06\x41mount\x18\x04 \x01(\x02\x12\x11\n\tDirection\x18\x05 \x01(\x08\"2\n\x08Historys\x12\x0e\n\x06Result\x18\x01 \x01(\x08\x12\x16\n\x04\x44\x61ta\x18\x02 \x03(\x0b\x32\x08.History24\n\nRpcService\x12&\n\x07Request\x12\x0c.DataRequest\x1a\r.DataResponseb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_DATARESPONSE = _descriptor.Descriptor(
  name='DataResponse',
  full_name='DataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='StatusCode', full_name='DataResponse.StatusCode', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Data', full_name='DataResponse.Data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Msg', full_name='DataResponse.Msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ErrorMsg', full_name='DataResponse.ErrorMsg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=47,
  serialized_end=148,
)


_EMPTYDATA_DATAENTRY = _descriptor.Descriptor(
  name='DataEntry',
  full_name='EmptyData.DataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EmptyData.DataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='EmptyData.DataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=199,
  serialized_end=242,
)

_EMPTYDATA = _descriptor.Descriptor(
  name='EmptyData',
  full_name='EmptyData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Data', full_name='EmptyData.Data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EMPTYDATA_DATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=242,
)


_DATAREQUEST_PARAMETERSENTRY = _descriptor.Descriptor(
  name='ParametersEntry',
  full_name='DataRequest.ParametersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='DataRequest.ParametersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataRequest.ParametersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=358,
)

_DATAREQUEST = _descriptor.Descriptor(
  name='DataRequest',
  full_name='DataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Parameters', full_name='DataRequest.Parameters', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_DATAREQUEST_PARAMETERSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=244,
  serialized_end=358,
)


_KLINE = _descriptor.Descriptor(
  name='Kline',
  full_name='Kline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='Kline.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ts', full_name='Kline.Ts', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Open', full_name='Kline.Open', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Close', full_name='Kline.Close', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='High', full_name='Kline.High', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Low', full_name='Kline.Low', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Amount', full_name='Kline.Amount', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Count', full_name='Kline.Count', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Volume', full_name='Kline.Volume', index=8,
      number=9, type=2, cpp_type=6, label=1,
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
  serialized_start=361,
  serialized_end=495,
)


_KLINES = _descriptor.Descriptor(
  name='Klines',
  full_name='Klines',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='Klines.Result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Data', full_name='Klines.Data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=497,
  serialized_end=543,
)


_HISTORY = _descriptor.Descriptor(
  name='History',
  full_name='History',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='History.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Ts', full_name='History.Ts', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Price', full_name='History.Price', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Amount', full_name='History.Amount', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Direction', full_name='History.Direction', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=545,
  serialized_end=628,
)


_HISTORYS = _descriptor.Descriptor(
  name='Historys',
  full_name='Historys',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Result', full_name='Historys.Result', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Data', full_name='Historys.Data', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=630,
  serialized_end=680,
)

_DATARESPONSE.fields_by_name['Data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EMPTYDATA_DATAENTRY.containing_type = _EMPTYDATA
_EMPTYDATA.fields_by_name['Data'].message_type = _EMPTYDATA_DATAENTRY
_DATAREQUEST_PARAMETERSENTRY.containing_type = _DATAREQUEST
_DATAREQUEST.fields_by_name['Parameters'].message_type = _DATAREQUEST_PARAMETERSENTRY
_KLINES.fields_by_name['Data'].message_type = _KLINE
_HISTORYS.fields_by_name['Data'].message_type = _HISTORY
DESCRIPTOR.message_types_by_name['DataResponse'] = _DATARESPONSE
DESCRIPTOR.message_types_by_name['EmptyData'] = _EMPTYDATA
DESCRIPTOR.message_types_by_name['DataRequest'] = _DATAREQUEST
DESCRIPTOR.message_types_by_name['Kline'] = _KLINE
DESCRIPTOR.message_types_by_name['Klines'] = _KLINES
DESCRIPTOR.message_types_by_name['History'] = _HISTORY
DESCRIPTOR.message_types_by_name['Historys'] = _HISTORYS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataResponse = _reflection.GeneratedProtocolMessageType('DataResponse', (_message.Message,), {
  'DESCRIPTOR' : _DATARESPONSE,
  '__module__' : 'tradingrpc_pb2'
  # @@protoc_insertion_point(class_scope:DataResponse)
  })
_sym_db.RegisterMessage(DataResponse)

EmptyData = _reflection.GeneratedProtocolMessageType('EmptyData', (_message.Message,), {

  'DataEntry' : _reflection.GeneratedProtocolMessageType('DataEntry', (_message.Message,), {
    'DESCRIPTOR' : _EMPTYDATA_DATAENTRY,
    '__module__' : 'tradingrpc_pb2'
    # @@protoc_insertion_point(class_scope:EmptyData.DataEntry)
    })
  ,
  'DESCRIPTOR' : _EMPTYDATA,
  '__module__' : 'tradingrpc_pb2'
  # @@protoc_insertion_point(class_scope:EmptyData)
  })
_sym_db.RegisterMessage(EmptyData)
_sym_db.RegisterMessage(EmptyData.DataEntry)

DataRequest = _reflection.GeneratedProtocolMessageType('DataRequest', (_message.Message,), {

  'ParametersEntry' : _reflection.GeneratedProtocolMessageType('ParametersEntry', (_message.Message,), {
    'DESCRIPTOR' : _DATAREQUEST_PARAMETERSENTRY,
    '__module__' : 'tradingrpc_pb2'
    # @@protoc_insertion_point(class_scope:DataRequest.ParametersEntry)
    })
  ,
  'DESCRIPTOR' : _DATAREQUEST,
  '__module__' : 'tradingrpc_pb2'
  # @@protoc_insertion_point(class_scope:DataRequest)
  })
_sym_db.RegisterMessage(DataRequest)
_sym_db.RegisterMessage(DataRequest.ParametersEntry)

Kline = _reflection.GeneratedProtocolMessageType('Kline', (_message.Message,), {
  'DESCRIPTOR' : _KLINE,
  '__module__' : 'tradingrpc_pb2'
  # @@protoc_insertion_point(class_scope:Kline)
  })
_sym_db.RegisterMessage(Kline)

Klines = _reflection.GeneratedProtocolMessageType('Klines', (_message.Message,), {
  'DESCRIPTOR' : _KLINES,
  '__module__' : 'tradingrpc_pb2'
  # @@protoc_insertion_point(class_scope:Klines)
  })
_sym_db.RegisterMessage(Klines)

History = _reflection.GeneratedProtocolMessageType('History', (_message.Message,), {
  'DESCRIPTOR' : _HISTORY,
  '__module__' : 'tradingrpc_pb2'
  # @@protoc_insertion_point(class_scope:History)
  })
_sym_db.RegisterMessage(History)

Historys = _reflection.GeneratedProtocolMessageType('Historys', (_message.Message,), {
  'DESCRIPTOR' : _HISTORYS,
  '__module__' : 'tradingrpc_pb2'
  # @@protoc_insertion_point(class_scope:Historys)
  })
_sym_db.RegisterMessage(Historys)


_EMPTYDATA_DATAENTRY._options = None
_DATAREQUEST_PARAMETERSENTRY._options = None

_RPCSERVICE = _descriptor.ServiceDescriptor(
  name='RpcService',
  full_name='RpcService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=682,
  serialized_end=734,
  methods=[
  _descriptor.MethodDescriptor(
    name='Request',
    full_name='RpcService.Request',
    index=0,
    containing_service=None,
    input_type=_DATAREQUEST,
    output_type=_DATARESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_RPCSERVICE)

DESCRIPTOR.services_by_name['RpcService'] = _RPCSERVICE

# @@protoc_insertion_point(module_scope)
