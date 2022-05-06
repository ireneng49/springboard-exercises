const addCommas = require("./addCommas");

describe("#addCommas", () => {
  test("it is a function", () => {
    expect(typeof addCommas).toBe("function");
  });
  test("Adds commas", () => {
    const commaStr1 = addCommas(111222333)
    expect(commaStr1).toEqual('111,222,333')
    const commaStr2 = addCommas(1234)
    expect(commaStr2).toEqual('1,234')
  });

  test("Wont add commas if not needed", () => {
    const commaStr1 = addCommas(111)
    expect(commaStr1).toEqual('111')
  });

  test("Handles negatives", () => {
    const commaStr1 = addCommas(-111222333)
    expect(commaStr1).toEqual('-111,222,333')
  });

  test("Handles decimals", () => {
    const commaStr1 = addCommas(111222333.1234)
    expect(commaStr1).toEqual('111,222,333.1234')
  });

  test("Handles negatives and decimals", () => {
    const commaStr1 = addCommas(-111222333.1234)
    expect(commaStr1).toEqual('-111,222,333.1234')
  });
});
