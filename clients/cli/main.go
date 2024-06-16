package main

import (
	"fmt"
	"os"
)

func main() {
	argCount := len(os.Args)

	fmt.Println("CLI Client")
	fmt.Println("Number of arguments:", argCount)
	fmt.Println("Arguments:", os.Args)
}
