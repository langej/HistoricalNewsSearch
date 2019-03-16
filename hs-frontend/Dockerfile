# build angular

FROM node:10 as node

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# build nginx

FROM nginx:1.15.7-alpine

COPY --from=node /usr/src/app/dist/hs-frontend /usr/share/nginx/html

COPY --from=node /usr/src/app/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

ENTRYPOINT ["nginx"]
CMD ["-g", "daemon off;"]