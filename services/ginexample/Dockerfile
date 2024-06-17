FROM golang:1.21

WORKDIR /app

COPY go.mod go.sum ./

RUN go clean -modcache
RUN go mod download

COPY . ./

RUN go test

RUN go build -o ./ginexample

EXPOSE 8000

ENTRYPOINT [ "go", "run", "." ]
