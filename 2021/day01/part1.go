package main

import (
	"bufio"
	// "fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var depths []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		depth, _ := strconv.Atoi(scanner.Text())
		depths = append(depths, depth)
	}
	if err := scanner.Err(); err != nil {
		panic(err)
	}

	// fmt.Printf("%v", depths)

	count := 0
	prev := depths[0]
	for _, depth := range depths[1:] {
		if depth > prev {
			count++
		}
		prev = depth
	}
	println(count)
}
