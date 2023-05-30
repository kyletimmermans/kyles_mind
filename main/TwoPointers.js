/*

Introduction
------------

The name two pointers does the technique justice, as it is exactly as it sounds.
It's the use of two different pointers (usually to keep track of array or string indices)
to solve a problem involving said indices with the benefit of saving time and space.


When do we use it?
------------------

In many problems involving collections such as arrays or lists,
we have to analyze each element of the collection compared to its other elements.

The two-pointer technique is efficient because are able to process two elements per loop
instead of just one. Common patterns in the two-pointer approach entail:

	1. Two pointers, each starting from the beginning and the end until they both meet.
	2. One pointer moving at a slow pace, while the other pointer moves at twice the speed.

These patterns can be used for string or array questions. They can also be streamlined and made
more efficient by iterating through two parts of an object simultaneously. You can see this in the
Two Sum problem or Reverse a String problems.

E.g.

    Pointer 1  Pointer 2
     Index 0	Index 4
       v           v
arr = [1, 3, 4, 8, 9]

Via https://algodaily.com/lessons/using-the-two-pointer-technique

*/


/* ----------------------------- */


/* 
	Code via @AlgoJS on YouTube

	Problem: Find which two elements equal 0 when added together
	
	Two Pointer Technique
*/

const arr = [-10, -8, -3, 3, 4, 5]; //sorted

let left = 0;
let right = arr.length-1; // We start at 0, shift all down 1

// Until we meet the pointers in the middle
while (left < right) {
	const sum = arr[left]+arr[right];
	if (sum === 0) {
		console.log(arr[left]);
		console.log(arr[right]);
		break;
	}else if (sum < 0) {
		left++; // If too small, get a bigger element
	}else if (sum > 0) {
		right--; // If too big, get a smaller element
	}
}
