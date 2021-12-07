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
	min_crab := math.MaxInt
	max_crab := math.MinInt
	for _, crab := range crabs_raw {
		c, err := strconv.Atoi(crab)
		if err != nil {
			panic(err)
		}
		// find lowest crab position
		if c < min_crab {
			min_crab = c
		}
		// find highest crab position
		if c > max_crab {
			max_crab = c
		}
		crabs = append(crabs, c)
	}

	// find minimal move
	min_cost := math.MaxInt
	for pos := min_crab; pos < max_crab; pos++ {
		crab_cost := 0
		for _, c := range crabs {
			// ensure horizontal distance difference is positive
			diff := c - pos
			if diff < 0 {
				diff *= -1
			}
			/* NOTE: triangle number formula
			 * prev_diff -> new_diff (one more than before)
			 * 0 -> 0
			 * 1 -> 1 = 1 + 0
			 * 2 -> 3 = 2 + 1
			 * 3 -> 6 = 3 + 2 + 1
			 * 4 -> 10 = 4 + 3 + 2 + 1
			 */
			crab_cost += diff * (diff + 1) / 2
		}
		// update minimal move
		if crab_cost < min_cost {
			min_cost = crab_cost
		}
	}

	println(min_cost)
}
