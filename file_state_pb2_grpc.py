# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import file_state_pb2 as file__state__pb2


class FileStateStub(object):
    """The FileState service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ExistsInState = channel.unary_unary(
                '/FileState/ExistsInState',
                request_serializer=file__state__pb2.ExistsInStateRequest.SerializeToString,
                response_deserializer=file__state__pb2.ExistsInStateResponse.FromString,
                )


class FileStateServicer(object):
    """The FileState service definition.
    """

    def ExistsInState(self, request, context):
        """RPC service with request/response information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileStateServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ExistsInState': grpc.unary_unary_rpc_method_handler(
                    servicer.ExistsInState,
                    request_deserializer=file__state__pb2.ExistsInStateRequest.FromString,
                    response_serializer=file__state__pb2.ExistsInStateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FileState', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class FileState(object):
    """The FileState service definition.
    """

    @staticmethod
    def ExistsInState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/FileState/ExistsInState',
            file__state__pb2.ExistsInStateRequest.SerializeToString,
            file__state__pb2.ExistsInStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
