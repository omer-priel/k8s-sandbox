package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	fmt.Println("INFO: Starting server on 8000")
	r := gin.Default()
	r.GET("/", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"service": "gin-example",
			"version": "0.1.0",
		})
	})
	r.Run("0.0.0.0:8000")
}
