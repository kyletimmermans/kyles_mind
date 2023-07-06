package main

import (
	"flag"
	"fmt"
)

/*

If we have a command-line program that takes multiple
flags, but we want to check if only one flag is set,
and that no other flags are set, we can create a counter
variable that keeps track of the number of flags that are
set, instead of writing multiple if-statement conditions
e.g. (a && !b && !c && !d)

We can do this because it doesn't matter which flag
is the single-set flag, rather how many are set. And
since we are dealing with "how many", we just make sure
that the number of set flags doesn't go over 1, and
that solves the problem of checking that only one flag
is set.

*/

func main() {
	a := flag.Bool("a", false, "Flag a")
	b := flag.Bool("b", false, "Flag b")
	c := flag.Bool("c", false, "Flag c")
	d := flag.Bool("d", false, "Flag d")

	// Parse the flags
	flag.Parse()

	// Count the number of set flags
	setFlags := 0
	if *a {
		setFlags++
	}
	if *b {
		setFlags++
	}
	if *c {
		setFlags++
	}
	if *d {
		setFlags++
	}

	// Check if wonly one of the flags is set
	if setFlags == 1 {
		fmt.Println("Valid flag combination.")
	} else {
		fmt.Println("Invalid flag combination. Please set only one of the flags: a, b, c, or d.")
	}
}
