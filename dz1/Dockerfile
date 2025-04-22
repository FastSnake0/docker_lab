# Сборка Python из исходников
FROM alpine:3.19 as builder

RUN apk add --no-cache \
    build-base \
    openssl-dev \
    bzip2-dev \
    zlib-dev \
    xz-dev \
    libffi-dev \
    wget \
    readline-dev \
    ncurses-dev \
    libuuid \
    sqlite-dev \
    lzlib \
    linux-headers \
    make

WORKDIR /build

ENV PYTHON_VERSION=3.12.2
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz && \
    tar -xzf Python-${PYTHON_VERSION}.tgz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --prefix=/opt/python --enable-optimizations --with-lto && \
    make -j$(nproc) && \
    make install

# Минимальный контейнер
FROM scratch

COPY --from=builder /opt/python /opt/python
COPY --from=builder /lib /lib
COPY --from=builder /usr/lib /usr/lib

COPY main.py /main.py

ENTRYPOINT ["/opt/python/bin/python3", "/main.py"]