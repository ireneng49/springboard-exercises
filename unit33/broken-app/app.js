const express = require("express");
const axios = require("axios");
const middleware = require("./middleware");
const app = express();

app.use(express.json());

app.post("/", middleware.checkBodyReq, async (req, res, next) => {
  try {

    const promises = req.body.developers.map((developer) => {
      return axios.get(`https://api.github.com/users/${developer}`);
    });

    const responses = await Promise.all(promises);

    const devsData = responses.map((response) => ({
      name: response.data.name,
      bio: response.data.bio,
    }));

    return res.json(devsData);
  } catch (err) {
    next(err);
  }
});

app.use((req, res, next) => {
  const err = new Error("Page not found", 404);
  next(err);
});

app.use((err, rep, res, next) => {
  next(err);
});

app.listen(3000, () => {
  console.log("Starting server 3000");
});
