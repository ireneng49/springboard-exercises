const timeWord = require('./timeWord');

describe("timeword", () => {
  test('it is a function', () => {
    expect(typeof timeWord).toBe('function');
  });
  test("00:00 --> midnight", () => {
    expect(timeWord("00:00")).toEqual("midnight");
  });
  test("00:12 --> twelve twelve AM", () => {
    expect(timeWord("00:12")).toEqual("twelve twelve AM");
  });
  test("01:00 --> one o'clock AM", () => {
    expect(timeWord("01:00")).toEqual("one o'clock AM");
  });
  test("06:01 --> six oh one AM", () => {
    expect(timeWord("06:01")).toEqual("six oh one AM");
  });
  test("06:10 --> six ten AM", () => {
    expect(timeWord("06:10")).toEqual("six ten AM");
  });
  test("06:18 --> six eighteen AM", () => {
    expect(timeWord("06:18")).toEqual("six eighteen AM");
  });
  test("06:30 --> six thirty AM", () => {
    expect(timeWord("06:30")).toEqual("six thirty AM");
  });
  test("10:34 --> ten thirty four AM", () => {
    expect(timeWord("10:34")).toEqual("ten thirty four AM");
  });
  test("12:00 --> noon", () => {
    expect(timeWord("12:00")).toEqual("noon");
  });
  test("12:09 --> twelve oh nine PM", () => {
    expect(timeWord("12:09")).toEqual("twelve oh nine PM");
  });
  test("23:23 --> eleven twenty three PM", () => {
    expect(timeWord("23:23")).toEqual("eleven twenty three PM");
  });
});