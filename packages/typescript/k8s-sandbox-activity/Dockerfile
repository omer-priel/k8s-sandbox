FROM node:21

WORKDIR /app

RUN npm install typescript @types/node
RUN npm install eslint @eslint/js prettier eslint-config-prettier eslint-plugin-prettier @typescript-eslint/eslint-plugin

COPY src /app/src
COPY .prettierrc.json /app
COPY eslint.config.js /app
COPY package.json /app
COPY tsconfig.json /app

RUN npm run eslint:lint

ENTRYPOINT ["echo", "Linting passed"]
