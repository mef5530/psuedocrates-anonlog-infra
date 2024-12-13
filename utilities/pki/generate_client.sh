openssl genrsa -out ../../anonalog_client/pki/client.key 2048

openssl req -new -key ../../anonalog_client/pki/client.key \
    -config client_cert.conf \
    -out ../../anonalog_client/pki/client.csr

openssl x509 -req -in ../../anonalog_client/pki/client.csr \
    -CA ../../ca/ca.crt -CAkey ../../ca/ca.key -CAcreateserial \
    -out ../../anonalog_client/pki/client.crt -days 365 -sha256 \
    -extfile client_cert.conf -extensions req_ext