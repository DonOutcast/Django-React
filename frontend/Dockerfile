FROM node:21.4.0-bookworm

RUN bash -c "apt update -y && apt install git -y"

WORKDIR /web
RUN export PATH=/web/node_modules/.bin:$PATH

COPY ./package.json ./package.json
COPY ./yarn.lock ./yarn.lock

RUN yarn cache clean
RUN yarn install --check-cache --network-concurrency 4

COPY . .

RUN yarn build

EXPOSE 3095

CMD yarn start
