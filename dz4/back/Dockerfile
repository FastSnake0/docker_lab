# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --prefix=/install -r requirements.txt

COPY app.py .

# Stage 2: Minimal runtime
FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# install runtime dependencies
RUN apk add --no-cache libstdc++ libgcc

# copy installed packages from builder
COPY --from=builder /install /usr/local
COPY --from=builder /build/app.py .
EXPOSE 5000
CMD ["python", "app.py"]