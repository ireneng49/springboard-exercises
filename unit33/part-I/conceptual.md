### Conceptual Exercise

Answer the following questions below:

- What are some ways of managing asynchronous code in JavaScript?

  We can use Asynchronuos Callbacks, Promises(solves chaining a number of function calls in callbacks), and Async and Await

- What is a Promise?

  Promise is a guarantee(placeholder) of future value. It is an object. There are 3 states for a promise:
  1. pending
  2. resolved
  3. rejected
  We can access the resolved or rejected values by chaining method .then at the end of the promise. When we send an axios request(axios.method), we get a promise back and we can chain .then to access the value.

- What are the differences between an async function and a regular function?

  Async function always return a promise - the value can be resolved or rejected and you will usually use it with await. Await will pause the execution inside of the async function until we get a response from a promise comes back. Regular functions just work on its own and return what you define it to return or return nothing or undefined.

- What is the difference between Node.js and Express.js?
  
  Express. js is a framework based on Node. js for which is used for building web-application using approaches and principles of Node. js.

  Node.js is an open source and cross-platform runtime environment for executing JavaScript code outside of a browser. We often use Node.js for building back-end services like APIs like Web App or Mobile App.

  Express is a small framework that sits on top of Node.js’s web server functionality to simplify its APIs and add helpful new features. It makes it easier to organize your application’s functionality with middle ware and routing. It adds helpful utilities to Node.js’s HTTP objects.

  credit: [geeksforgeeks.org](https://www.geeksforgeeks.org/node-js-vs-express-js/)

- What is the error-first callback pattern?

        function(err, optional param1, optional param2....){
          if(err){
            code here
          }
        }
  

- What is middleware?

It is a set of code that runs in the middle of the request/response cycle. It is functions that get access to request and response objects and can also call the "next" function


- What does the `next` function do?

next is the third parameter in a function. It moves on to the next matching routes/error handler

- What are some issues with the following code? (consider all aspects: performance, structure, naming, etc)

```js
async function getUsers() {
  const elie = await $.getJSON('https://api.github.com/users/elie');
  const joel = await $.getJSON('https://api.github.com/users/joelburton');
  const matt = await $.getJSON('https://api.github.com/users/mmmaaatttttt');

  return [elie, matt, joel];
}
```
Performance: I believe that it's not super efficient when we can use Promise.all() at once for 3 requests becuase these individual requests are independent.

Structure: I would just extract which part of the data I want instead of putting the whole object into an array.

Also, I would declare a variable for an empty array at the top of the function and push the data after I get back using .foEach() for all the responses I get back at once. We can just return the data using that variable name too becuase we push everything to that array already

Name: Naming should be more specific based on which piece of data you want for example if you just want the id part, it should just say elieID or if you want just login part, it should say elieLogin