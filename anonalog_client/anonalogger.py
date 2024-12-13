import grpc
import anonalog_client.log_methods_pb2
import anonalog_client.log_methods_pb2_grpc

class Anonalogger():
    def __init__(self, client_crt_fp, client_key_fp, ca_crt_fp, server_ip_port):
        with open(client_crt_fp, 'rb') as f:
            self._client_crt = f.read()
        with open(client_key_fp, 'rb') as f:
            self._client_key = f.read()
        with open(ca_crt_fp, 'rb') as f:
            self._ca_crt = f.read()
        
        self._client_credentials = grpc.ssl_channel_credentials(
            root_certificates=self._ca_crt,
            private_key=self._client_key,
            certificate_chain=self._client_crt
        )

        self._channel = grpc.secure_channel(server_ip_port, self._client_credentials)
        self._stub = log_methods_pb2_grpc.LogServiceStub(self._channel)

        def log_register(self, username, password=''):
            request = log_methods_pb2.RegisterRequest(username=username, password=password)
            response = self._stub.Register(request)
            return response
        
        def log_login(self, username, password=''):
            request = log_methods_pb2.LoginRequest(username=username, password=password)
            response = self._stub.Login(request)
            return response

        def log_store_user_data(self, data, username, name, bio):
            request = log_methods_pb2.StoreUserDataRequest(data=data, username=username, name=name, bio=bio)
            response = self._stub.StoreUserData(request)
            return response

        def log_chatbot_initialize(self, user_bio, selected_scenario, username, chatbot_id):
            request = log_methods_pb2.ChatbotInitializeRequest(user_bio=user_bio, selected_scenario=selected_scenario, username=username, chatbot_id=chatbot_id)
            response = self._stub.ChatbotInitialize(request)
            return response
        
        def log_chatbot_send(self, chatbot_id, message, model_response):
            request = log_methods_pb2.ChatbotSendRequest(chatbot_id=chatbot_id, message=message, response=model_response)
            response = self._stub.ChatbotSend(request)
            return response

        def log_ethics_engine_send(self, chatbot_id, background, dilemma, options, desired_result, model_response):
            request = log_methods_pb2.EthicsEngineSendRequest(chatbot_id=chatbot_id, background=background, dilemma=dilemma, options=options, desired_result=desired_result, response=model_response)
            response = self._stub.EthicsEngineSend(request)
            return response