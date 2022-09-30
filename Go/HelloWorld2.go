package main

import "fmt"

func main() {
	msg := []string{"H", "e", "l", "l", "o", " ", "W", "o", "r", "l", "d", "!"}

	for _, char := range msg {
		fmt.Print(char)
	}
}
