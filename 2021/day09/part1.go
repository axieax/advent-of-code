package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, _ := os.Open("input.txt")
	var arr [][]int
	// scan input line by line
	for {
		var line string
		_, err := fmt.Fscanln(file, &line)
		if err != nil {
			break
		}
		// split line into array of ints
		var nums []int
		for _, digit := range line {
			num, _ := strconv.Atoi(string(digit))
			nums = append(nums, num)
		}
		// add to array
		arr = append(arr, nums)
	}

	var collected []int
	i_max := len(arr)
	for i := 0; i < i_max; i++ {
		j_max := len(arr[i])
		for j := 0; j < j_max; j++ {
			val := arr[i][j]
			// check up
			if i != 0 && arr[i-1][j] <= val {
				continue
			}
			// check right
			if j != j_max-1 && arr[i][j+1] <= val {
				continue
			}
			// check down
			if i != i_max-1 && arr[i+1][j] <= val {
				continue
			}
			// check left
			if j != 0 && arr[i][j-1] <= val {
				continue
			}
			collected = append(collected, val)
		}
	}

	// sum of risk level
	sum := 0
	for _, val := range collected {
		sum += val + 1
	}
	println(sum)
}
