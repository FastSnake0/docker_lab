FROM python:3.12-slim as builder

RUN mkdir -p /minimal/lib /minimal/lib64 /minimal/usr/local/lib /minimal/usr/local/bin

# 1. Python бинарник
RUN cp /usr/local/bin/python3.12 /minimal/python3

# 2. Shared библиотеки Python
RUN cp /usr/local/lib/libpython3.12.so.1.0 /minimal/lib/

# 3. Стандартная библиотека Python
RUN cp -r /usr/local/lib/python3.12 /minimal/usr/local/lib/python3.12

# 4. C-библиотеки
RUN cp /lib/x86_64-linux-gnu/libc.so.6 /minimal/lib/
RUN cp /lib/x86_64-linux-gnu/libm.so.6 /minimal/lib/

# 5. Dynamic linker
RUN cp /lib64/ld-linux-x86-64.so.2 /minimal/lib64/

COPY main.py /minimal/main.py

FROM scratch
COPY --from=builder /minimal/ /

ENTRYPOINT ["/python3", "/main.py"]