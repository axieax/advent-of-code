package main

import (
	"math"
	"os"
	"strconv"
	"strings"
)

func main() {
	data, err := os.ReadFile("input.txt")
	if err != nil {
		panic(err)
	}

	// split by comma and convert elements to int
	crabs_raw := strings.Split(strings.TrimSuffix(string(data), "\n"), ",")
	var crabs []int
	for _, crab := range crabs_raw {
		c, err := strconv.Atoi(crab)
		if err != nil {
			panic(err)
		}
		crabs = append(crabs, c)
	}

	// find minimal move
	min_cost := math.MaxInt
	for _, c1 := range crabs {
		crab_cost := 0
		for _, c2 := range crabs {
			// ensure horizontal distance difference is positive
			diff := c2 - c1
			if diff < 0 {
				diff *= -1
			}
			crab_cost += diff
		}
		// update minimal move
		if crab_cost < min_cost {
			min_cost = crab_cost
		}
	}

	println(min_cost)
}
