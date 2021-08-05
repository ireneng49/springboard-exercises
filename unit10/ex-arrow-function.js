/** ES5 Map Callback
function double(arr) {
  return arr.map(function(val) {
    return val * 2;
  });
}
**/

//ES2015 Arrow Functions Shorthand
const double = arr => arr.map(val => val * 2);

/**
  function squareAndFindEvens(numbers){
  var squares = numbers.map(function(num){
    return num ** 2;
  });
  var evens = squares.filter(function(square){
    return square % 2 === 0;
  });
  return evens;
}
 **/

// version 1.0
const squareAndFindEvens = (numbers) => {
    var squares = numbers.map(function(num){
        return num ** 2;
    });
    var evens = squares.filter(function(square){
        return square % 2 === 0;
    });
    return evens;
}

// version 1.1
const squareAndFindEvens = (numbers) => {
    var squares = numbers.map((num) => {
        return num ** 2;
    });
    var evens = squares.filter((square) => {
        return square % 2 === 0;
    });
    return evens;
}

// version 1.2
const squareAndFindEvens = numbers => {
    var squares = numbers.map(num => {
        return num ** 2;
    });
    var evens = squares.filter(square => {
        return square % 2 === 0;
    });
    return evens;
}

// version 1.3
const squareAndFindEvens = numbers => {
    var squares = numbers.map(num => num ** 2);
    return squares.filter(square => square % 2 === 0);
}

// final version
const squareAndFindEvens = numbers => numbers.map(num => num ** 2).filter(square => square % 2 === 0);