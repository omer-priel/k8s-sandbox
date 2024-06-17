FROM node:21

WORKDIR /app

RUN npm install fastify
RUN npm install prettier

COPY src /app/src
COPY package.json /app
COPY .prettierrc.json /app

EXPOSE 8000

ENTRYPOINT ["node", "src/index.js"]
