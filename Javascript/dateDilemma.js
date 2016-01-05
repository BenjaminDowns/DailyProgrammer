function formatDate(date) {

  // helper functions for padding
  function makePad(num) {
    return num.length < 2 ? "0" + num.toString() : num
  }
  
  // assumes no dates before 2000
  function makeYearPad(num) {
    return num.length < 4 ? "20" + num.toString() : num
  }

  // parse and format the date
  var splitDate = date.split(/[^\d]/)
  var year, month, day
  
  if (splitDate[0].length === 4) {
    year = makeYearPad(splitDate[0])
    month = makePad(splitDate[1])
    day = makePad(splitDate[2])
  } else {
    month = makePad(splitDate[0])
    day = makePad(splitDate[1])
    year = makeYearPad(splitDate[2])
  }
  
  return year + '-' + month + '-' + day
}

console.log(formatDate("2012 3 1"))
console.log(formatDate("2/13/15"))
console.log(formatDate("1-31-10"))
console.log(formatDate("5 10 2015"))
console.log(formatDate("2012 3 17"))
console.log(formatDate("2001-01-01"))
console.log(formatDate("2008/01/07"))