# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from anonalog_client import log_methods_pb2 as anonalog__client_dot_log__methods__pb2

GRPC_GENERATED_VERSION = '1.68.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in anonalog_client/log_methods_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LogServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/log_methods.LogService/Register',
                request_serializer=anonalog__client_dot_log__methods__pb2.RegisterRequest.SerializeToString,
                response_deserializer=anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
                _registered_method=True)
        self.Login = channel.unary_unary(
                '/log_methods.LogService/Login',
                request_serializer=anonalog__client_dot_log__methods__pb2.LoginRequest.SerializeToString,
                response_deserializer=anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
                _registered_method=True)
        self.StoreUserData = channel.unary_unary(
                '/log_methods.LogService/StoreUserData',
                request_serializer=anonalog__client_dot_log__methods__pb2.StoreUserDataRequest.SerializeToString,
                response_deserializer=anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
                _registered_method=True)
        self.ChatbotInitialize = channel.unary_unary(
                '/log_methods.LogService/ChatbotInitialize',
                request_serializer=anonalog__client_dot_log__methods__pb2.ChatbotInitializeRequest.SerializeToString,
                response_deserializer=anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
                _registered_method=True)
        self.ChatbotSend = channel.unary_unary(
                '/log_methods.LogService/ChatbotSend',
                request_serializer=anonalog__client_dot_log__methods__pb2.ChatbotSendRequest.SerializeToString,
                response_deserializer=anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
                _registered_method=True)
        self.EthicsEngineSend = channel.unary_unary(
                '/log_methods.LogService/EthicsEngineSend',
                request_serializer=anonalog__client_dot_log__methods__pb2.EthicsEngineSendRequest.SerializeToString,
                response_deserializer=anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
                _registered_method=True)


class LogServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StoreUserData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChatbotInitialize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChatbotSend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EthicsEngineSend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=anonalog__client_dot_log__methods__pb2.RegisterRequest.FromString,
                    response_serializer=anonalog__client_dot_log__methods__pb2.StandardResponse.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=anonalog__client_dot_log__methods__pb2.LoginRequest.FromString,
                    response_serializer=anonalog__client_dot_log__methods__pb2.StandardResponse.SerializeToString,
            ),
            'StoreUserData': grpc.unary_unary_rpc_method_handler(
                    servicer.StoreUserData,
                    request_deserializer=anonalog__client_dot_log__methods__pb2.StoreUserDataRequest.FromString,
                    response_serializer=anonalog__client_dot_log__methods__pb2.StandardResponse.SerializeToString,
            ),
            'ChatbotInitialize': grpc.unary_unary_rpc_method_handler(
                    servicer.ChatbotInitialize,
                    request_deserializer=anonalog__client_dot_log__methods__pb2.ChatbotInitializeRequest.FromString,
                    response_serializer=anonalog__client_dot_log__methods__pb2.StandardResponse.SerializeToString,
            ),
            'ChatbotSend': grpc.unary_unary_rpc_method_handler(
                    servicer.ChatbotSend,
                    request_deserializer=anonalog__client_dot_log__methods__pb2.ChatbotSendRequest.FromString,
                    response_serializer=anonalog__client_dot_log__methods__pb2.StandardResponse.SerializeToString,
            ),
            'EthicsEngineSend': grpc.unary_unary_rpc_method_handler(
                    servicer.EthicsEngineSend,
                    request_deserializer=anonalog__client_dot_log__methods__pb2.EthicsEngineSendRequest.FromString,
                    response_serializer=anonalog__client_dot_log__methods__pb2.StandardResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'log_methods.LogService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('log_methods.LogService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LogService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/log_methods.LogService/Register',
            anonalog__client_dot_log__methods__pb2.RegisterRequest.SerializeToString,
            anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/log_methods.LogService/Login',
            anonalog__client_dot_log__methods__pb2.LoginRequest.SerializeToString,
            anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def StoreUserData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/log_methods.LogService/StoreUserData',
            anonalog__client_dot_log__methods__pb2.StoreUserDataRequest.SerializeToString,
            anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ChatbotInitialize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/log_methods.LogService/ChatbotInitialize',
            anonalog__client_dot_log__methods__pb2.ChatbotInitializeRequest.SerializeToString,
            anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ChatbotSend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/log_methods.LogService/ChatbotSend',
            anonalog__client_dot_log__methods__pb2.ChatbotSendRequest.SerializeToString,
            anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def EthicsEngineSend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/log_methods.LogService/EthicsEngineSend',
            anonalog__client_dot_log__methods__pb2.EthicsEngineSendRequest.SerializeToString,
            anonalog__client_dot_log__methods__pb2.StandardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
