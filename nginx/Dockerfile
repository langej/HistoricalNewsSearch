FROM nginx:1.15.7-alpine

RUN rm -rf /usr/share/nginx/html/*

COPY ./nginx/nginx.conf /etc/nginx/nginx.conf

COPY ./hs-frontend/dist/hs-frontend /usr/share/nginx/html

EXPOSE 80 443

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]