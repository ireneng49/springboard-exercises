/** Turn a string of 24h time into words.
 *  You can trust that you'll be given a valid string (it will always have a two-digit hour 00-23 and a two-digit minute 00-59). Hours 0-11 are am, and hours 12-23 are pm.
 */

const { convertHours, hoursToWords, minutesToWords, getAmPm } = require("./helpers");

/** 
 * fcn timeWord 
 * Input a string that expresses military time
 * The fcn returns 
 */
function timeWord(timeString) {
  // pull off hours and minutes as strings
  const hours = timeString.slice(0, 2);  
  const minutes = timeString.slice(3, 5);

  // convert hours and minutes to words
  const newHours = convertHours(hours);  // string of two digits
  const hoursWord = hoursToWords(hours, newHours, minutes);  // hours in words
  const minutesWord = minutesToWords(hours, minutes); // minutes in words

  // get AM/PM; use military hours as input
  const meridian = getAmPm(hours, hoursWord);  
  
  let result = hoursWord + " " + minutesWord + " " + meridian;
  // remove extra spaces in result
  result = result.replace(/\s+/g,' ');
  result = result.trimEnd();
  // return result
  return result;
}

module.exports = timeWord;