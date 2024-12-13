#run from project root
python -m grpc_tools.protoc \
    --proto_path=. \
    --python_out=. \
    --grpc_python_out=. \
    anonalog_server/log_methods_pb2/log_methods.proto