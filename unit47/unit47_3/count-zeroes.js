/**
 * countZeroes
Given an array of 1s and 0s which has all 1s first followed by all 0s, write a function called countZeroes, which returns the number of zeroes in the array.

Constraints:

Time Complexity: O(log N)

Examples:

countZeroes([1,1,1,1,0,0]) // 2
countZeroes([1,0,0,0,0]) // 4
countZeroes([0,0,0]) // 3
countZeroes([1,1,1,1]) // 0
*/


function countZeroes(arr) {
  let firstzeroposition = firstzero(arr);
  if (firstzeropostion === -1){
      return 0;
  }
  return arr.length-firstzeroposition;
}

module.exports = countZeroes