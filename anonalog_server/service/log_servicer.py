import grpc
from concurrent import futures

from anonalog_server.log_methods_pb2 import log_methods_pb2_grpc
from anonalog_server.log_methods_pb2 import log_methods_pb2
from anonalog_server.anon.utilities import anonymize_data_field
from anonalog_server.model.store_log import store_log

class LogServicer(log_methods_pb2_grpc.LogServiceServicer):
    def Register(self, request, context):
        anon_fields = anonymize_data_field(username=request.username, password=request.password)
        store_log('register', anon_fields)
        return log_methods_pb2.StandardResponse(success=True, message='')
    
    def Login(self, request, context):
        anon_fields = anonymize_data_field(username=request.username, password=request.password)
        store_log('login', anon_fields)
        return log_methods_pb2.StandardResponse(success=True, message='')
    
    def StoreUserData(self, request, context):
        anon_fields = anonymize_data_field(data=request.data, username=request.username, name=request.name, bio=request.bio)
        store_log('store_user_data', anon_fields)
        return log_methods_pb2.StandardResponse(success=True, message='')

    def ChatbotInitialize(self, request, context):
        anon_fields = anonymize_data_field(user_bio=request.user_bio, selected_scenario=request.selected_scenario, username=request.username, chatbot_id=request.chatbot_id)
        store_log('chatbot_initialize', anon_fields)
        return log_methods_pb2.StandardResponse(success=True, message='')
    
    def ChatbotSend(self, request, context):
        anon_fields = anonymize_data_field(chatbot_id=request.chatbot_id, message=request.message, response=request.response)
        store_log('chatbot_send', anon_fields)
        return log_methods_pb2.StandardResponse(success=True, message='')
    
    def EthicsEngineSend(self, request, context):
        anon_fields = anonymize_data_field(chatbot_id=request.chatbot_id, background=request.background, dilemma=request.dilemma, options=request.options, desired_result=request.desired_result, response=request.response)
        store_log('ethics_engine_send', anon_fields)
        return log_methods_pb2.StandardResponse(success=True, message='')

def serve():
    with open('anonalog_server/pki/server.crt', 'rb') as f:
        server_crt = f.read()
    with open('anonalog_server/pki/server.key', 'rb') as f:
        server_key = f.read()
    with open('anonalog_server/pki/ca.crt', 'rb') as f:
        ca_cert = f.read()
    
    server_credentials = grpc.ssl_server_credentials(
        [(server_key, server_crt)],
        root_certificates=ca_cert,
        require_client_auth=True
    )

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    log_methods_pb2_grpc.add_LogServiceServicer_to_server(LogServicer(), server)
    server.add_secure_port('[::]:50051', server_credentials=server_credentials)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()