openssl genrsa -out ../../ca/ca.key 2048
openssl req -x509 -new -nodes -key ../../ca/ca.key -sha256 -days 365 \
    -subj "/CN=localhost" \
    -out ../../ca/ca.crt