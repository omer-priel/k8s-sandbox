package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type rootHandler struct{}

func (h *rootHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("content-type", "application/json")
	switch r.Method {
		case http.MethodGet:
			fmt.Println("INFO: GET /")
			data := make(map[string]interface{})
			data["service"] = "gohttp-example"
			data["version"] = "0.1.0"

			jsonBytes, err := json.Marshal(data)
			if err != nil {
				w.WriteHeader(http.StatusInternalServerError)
				w.Write([]byte("{\"error\": \"Internal Server Error\"}"))
			}

			w.WriteHeader(http.StatusOK)
			w.Write(jsonBytes)
			return
		default:
			fmt.Println("ERROR: Method not allowed")
			w.WriteHeader(http.StatusMethodNotAllowed)
			return
	}
}

func main() {
	fmt.Println("INFO: Starting server on 8000")
	mux := http.NewServeMux()

	root := &rootHandler{}

	mux.Handle("/", root)

	http.ListenAndServe(":8000", mux)
}
