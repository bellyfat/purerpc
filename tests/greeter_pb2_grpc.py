# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import greeter_pb2 as greeter__pb2


class GreeterStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SayHello = channel.unary_unary(
        '/Greeter/SayHello',
        request_serializer=greeter__pb2.HelloRequest.SerializeToString,
        response_deserializer=greeter__pb2.HelloReply.FromString,
        )
    self.SayHelloGoodbye = channel.unary_stream(
        '/Greeter/SayHelloGoodbye',
        request_serializer=greeter__pb2.HelloRequest.SerializeToString,
        response_deserializer=greeter__pb2.HelloReply.FromString,
        )
    self.SayHelloToMany = channel.stream_stream(
        '/Greeter/SayHelloToMany',
        request_serializer=greeter__pb2.HelloRequest.SerializeToString,
        response_deserializer=greeter__pb2.HelloReply.FromString,
        )
    self.SayHelloToManyAtOnce = channel.stream_unary(
        '/Greeter/SayHelloToManyAtOnce',
        request_serializer=greeter__pb2.HelloRequest.SerializeToString,
        response_deserializer=greeter__pb2.HelloReply.FromString,
        )


class GreeterServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SayHello(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHelloGoodbye(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHelloToMany(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SayHelloToManyAtOnce(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SayHello': grpc.unary_unary_rpc_method_handler(
          servicer.SayHello,
          request_deserializer=greeter__pb2.HelloRequest.FromString,
          response_serializer=greeter__pb2.HelloReply.SerializeToString,
      ),
      'SayHelloGoodbye': grpc.unary_stream_rpc_method_handler(
          servicer.SayHelloGoodbye,
          request_deserializer=greeter__pb2.HelloRequest.FromString,
          response_serializer=greeter__pb2.HelloReply.SerializeToString,
      ),
      'SayHelloToMany': grpc.stream_stream_rpc_method_handler(
          servicer.SayHelloToMany,
          request_deserializer=greeter__pb2.HelloRequest.FromString,
          response_serializer=greeter__pb2.HelloReply.SerializeToString,
      ),
      'SayHelloToManyAtOnce': grpc.stream_unary_rpc_method_handler(
          servicer.SayHelloToManyAtOnce,
          request_deserializer=greeter__pb2.HelloRequest.FromString,
          response_serializer=greeter__pb2.HelloReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Greeter', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))