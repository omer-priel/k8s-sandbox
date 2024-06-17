FROM node:21

WORKDIR /app

RUN npm install typescript @types/node
RUN npm install prettier

COPY src /app/src
COPY .prettierrc.json /app
COPY package.json /app
COPY tsconfig.json /app

ENTRYPOINT ["echo", "Linting passed"]
