FROM nginx:1.25

WORKDIR /app

COPY www/index.html /usr/share/nginx/html/index.html
COPY www/index.json /usr/share/nginx/html/index.json

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]
