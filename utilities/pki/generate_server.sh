openssl genrsa -out ../../anonalog_server/pki/server.key 2048

openssl req -new -key ../../anonalog_server/pki/server.key \
    -config server_cert.conf \
    -out ../../anonalog_server/pki/server.csr

openssl x509 -req -in ../../anonalog_server/pki/server.csr \
    -CA ../../ca/ca.crt -CAkey ../../ca/ca.key -CAcreateserial \
    -out ../../anonalog_server/pki/server.crt -days 365 -sha256 \
    -extfile server_cert.conf -extensions req_ext
