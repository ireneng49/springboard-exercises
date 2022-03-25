# Broken App Issues
1. there was no "error" param in catch
2. There was no generic error function
3. change variable names
   1.  'd' -> developer
   2.  'out' -> devsData
   3.  'r' -> response
   4.  'results' -> responses
4. I was unable to access req.body but I configured Express - app.use(express.json()), to parse data from the request to access req.body
5. "results" returns an array of promises so I use Promise.all() to get new resolved promises because these are independent requests
6. Since Express has a built-in method to turn the response we pass in as JSON, I use res.json() instead of res.send(JSON.stringify())
7. I use middleware for check if there is req.body.developers and if not we can throw error