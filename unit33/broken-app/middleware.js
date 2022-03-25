function checkBodyReq(req, res, next) {
  try {
    if (!req.body.developers) {
      throw new Error("Please check your request", 400);
    } else {
      return next();
    }
  } catch (e) {
    return next(e);
  }
}

module.exports = { checkBodyReq };
