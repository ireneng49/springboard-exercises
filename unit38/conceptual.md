### Conceptual Exercise

Answer the following questions below:

- What is a JWT?

A: A JSON web token is a way to add state to the stateless HTTP protocol to keep track of who is making a given request. We can use JWTs to make the logged in state persist across different requests and even different servers (when it makes sense to do so).
* The approach is different from using the session for this, as we did in Flask, because JWTs allow us to share authentication info across multiple APIs or hostnames.
* Example: (Although Google uses OAuth and not JWTs, this analogy is still applicable). Google has many different servers and many APIs, such as Google Drive, Gmail, Google Maps, Google Sites, etc., but a user has just one username and password that work for all the APIs and servers.  Furthermore, the user only needs to login once, and all of the servers will be able to recognize the user until the user logs out, because the logged in state is being shared across servers.
Without JWTs (or similar tool), the user would have to register for each of these APIs independently and login to each one independently of all the others.


- What is the signature portion of the JWT?  What does it do?

A: The signature portion of the JWT is a special encrypted code based on the header and payload data. A secret key value is used to generate the signature using a hashing algorithm. Because the secret key is kept secret, the signature is nearly impossible to guess, and so it is used on the server side to verify the identity of the sender of a request and also to make sure that the user's data has not been tampered with since it was last signed.


- If a JWT is intercepted, can the attacker see what's inside the payload?

A: Yes, anyone can easily decode the data in the payload.


- How can you implement authentication with a JWT?  Describe how it works at a high level.

A: After a user logs in, a signed JWT is generated and sent back to the client, where it is stored. We can then write logic to send the token back to the server with every request that user makes so that the server can authenticate the user's identity, verify logged in status, and authorize/restrict certain actions based on user's rights (e.g., admin rights).


- Compare and contrast unit, integration and end-to-end tests.

A: Similarities:
All three are ways of checking the functionality of the app and finding any bugs that exist. 
Differences:
They differ in how much code is touched in a single test and how sensitive they are to breaking when code in any one part of the app is edited.
* Unit tests are conceptually simpler than the other two types of tests; they test a single function. Because unit tests focus on a just a single function, they only way they can break is if that function is changed.
* Integration tests test the interaction of code from different parts of the app. For example, one could test whether a given route produces the expected result. To get to that result, many pieces from many files (e.g., authentication, route handling, data validation, database model methods) have to work correctly by themselves and in conjunction with each other. Integration tests are easier to break than unit tests, because they touch so many parts of an app.
* End-to-end tests are the trickiest, because they touch all parts of the application, and can break any time code is changed. End-to-end tests test the entire application flow from a user's perspective from beginning to end. 


- What is a mock? What are some things you would mock?

A: In software testing (primarily in unit testing), a mock is an object that takes the place of another object or dependency that is impractical or difficult to test. The mock simulates the behavior of the object it is taking the place of, but it allows us to have certainty about the return value by standardizing the behavior of a process/function/dependency.
A good candidate for mocking is a function or behavior that is out of our control, such as a function that involves some randomness or depends on an external tool/library to make AJAX requests. Reading/writing to files is another use case for mocking.


- What is continuous integration?
A: Continuous integration is the practice of merging in small code changes frequently, rather than merging in a large change at the end of a development cycle. It requires the code to be tested for each of these small changes.


- What is an environment variable and what are they used for?
A: An environment variable is one that we want to keep  secure, such as a secret key or API key or one whose value can change based on the environment (e.g, production environment, development environment, test environment).


- What is TDD? What are some benefits and drawbacks?
A: TDD stands for test-driven development. It's an approach to software development that involves focusing on completing a single feature or user story at a time.  For each story, write the tests first before doing any coding. Then, code the minimum amount to make the tests pass. Finally, refactor the code. 

**Benefits of TDD:**
1. The code will be written for easier testing right from the beginning.
2. The process forces the developer to organize their thinking by planning out how each feature should behave, including what the inputs and returned values should be.
3. When TDD is done well, it saves time in the long run by preventing bugs.

**Drawbacks of TDD:**
1. The code takes longer to write initially.
2. There's a learning curve to getting into the mindset of TDD.
3. If tests are not written well and strategically, many of the potential benefits of TDD are lost.


- What is the value of using JSONSchema for validation?

A: We need a schema validation system so that we prevent malformed data from making its way into our database or crashing our server.  We could do this with a lot of conditional logic in the code, but that would clutter up our app.  JSONSchema is a nice tool that we can use to specify the proper structure of our data, validate data against that schema, and provide helpful error messages when data does not validate.


- What are some ways to decide which code to test?

A: Shooting for 100% coverage by tests is not realistic; therefore, we need to prioritize testing the most important functionality. Also, we want to test the functionality of the routes of an API, not the changes made to the database directly. Integration testing accomplishes this.


- What are some differences between Web Sockets and HTTP?

A: Differences:
* Websockets have state that persists; HTTP is stateless. So, in HTTP we connect, make a request, get a response and then end the connection, but websockets keep that connection open for more requests to go through.
* Websockets can be very lightweight compared to HTTP.


- Did you prefer using Flask over Express? Why or why not (there is no right answer here --- we want to see how you think about technology)?
A: Hmmm. Good question.  There are aspects of both that I appreciate. I'll say Express for the following reasons:
1. It gives me more practice with JavaScript which is an inescapable language in web development.
2. I can use console.log for debugging.
3. The modularized approach (i.e., exporting modules and requiring them in another file) makes sense to me and feels more organized.
4. package.json is a cool concept!
5. There are no virtual environments in Node (at least so far). Setting up and using a venv was just one more step that took time in Flask.

