package main

import (
	"bufio"
	"os"
	"strconv"
)

const SLIDING_WINDOW_SIZE int = 3

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	var depths []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		depth, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}
		depths = append(depths, depth)
	}

	count := 0
	prev_window_sum := 0
	for _, d := range depths[:SLIDING_WINDOW_SIZE] {
		prev_window_sum += d
	}
	for i := 0; i < len(depths)-SLIDING_WINDOW_SIZE+1; i++ {
		window := depths[i : i+SLIDING_WINDOW_SIZE]
		window_sum := 0
		for _, d := range window {
			window_sum += d
		}
		if window_sum > prev_window_sum {
			count++
		}
		prev_window_sum = window_sum
	}
	println(count)
}
