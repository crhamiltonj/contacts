FROM nginx:1.11.3
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
COPY contact.conf /etc/nginx/conf.d/
