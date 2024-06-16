FROM node:21

WORKDIR /app

RUN npm install express
RUN npm install eslint prettier eslint-config-prettier eslint-plugin-prettier

COPY src /app/src
COPY package.json /app
COPY eslint.config.js /app
COPY .prettierrc.json /app

RUN npm run eslint:lint

EXPOSE 8000

ENTRYPOINT ["node", "src/index.js"]
