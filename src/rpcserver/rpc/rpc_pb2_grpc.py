# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from rpc import rpc_pb2 as rpc__pb2


class RPCserverStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.cluster = channel.unary_unary(
        '/rpcserver.RPCserver/cluster',
        request_serializer=rpc__pb2.ClusterRequest.SerializeToString,
        response_deserializer=rpc__pb2.Matrix.FromString,
        )


class RPCserverServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def cluster(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RPCserverServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'cluster': grpc.unary_unary_rpc_method_handler(
          servicer.cluster,
          request_deserializer=rpc__pb2.ClusterRequest.FromString,
          response_serializer=rpc__pb2.Matrix.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'rpcserver.RPCserver', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))