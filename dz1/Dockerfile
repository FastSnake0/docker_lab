# Сборка Python
FROM alpine:3.19 as builder

RUN apk add --no-cache \
    build-base \
    zlib-dev \
    libffi-dev \
    wget

WORKDIR /build

ENV PYTHON_VERSION=3.12.2
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -xzf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --prefix=/opt/python --disable-ipv6 --without-ensurepip && \
    make -j$(nproc) && \
    make install && \
    cd / && \
    rm -rf Python-${PYTHON_VERSION} Python-${PYTHON_VERSION}.tgz

# Минимальный runtime (только нужные файлы)
FROM scratch

COPY --from=builder /opt/python /opt/python
COPY --from=builder /lib/ld-musl-x86_64.so.1 /lib/
COPY --from=builder /usr/lib/libffi.so.8 /usr/lib/

COPY main.py /main.py

ENTRYPOINT ["/opt/python/bin/python3", "/main.py"]