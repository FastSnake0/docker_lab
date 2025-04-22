FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
RUN rm -rf /var/cache/apk/* /etc/nginx/conf.d/default.conf

# Здесь будто нет смысла в мультстейдж