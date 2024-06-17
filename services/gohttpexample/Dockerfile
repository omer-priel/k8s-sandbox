FROM golang:1.21

WORKDIR /app

COPY go.mod ./

RUN go clean -modcache
RUN go mod download

COPY . ./

RUN go test

RUN go build -o ./gohttpexample

EXPOSE 8000

ENTRYPOINT [ "go", "run", "." ]
