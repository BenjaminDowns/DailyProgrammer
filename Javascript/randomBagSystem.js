var bag = ['O', 'I', 'S', 'Z', 'L', 'J', 'T'];

function randomBag() {
  var output = ''
  var tempBag = []

  while (output.length < 50) {
    tempBag.length === 7 ? tempBag = [] : null
    var next = Math.floor((Math.random() * bag.length))
    
    while (tempBag.indexOf(bag[next]) > -1) {
      next = Math.floor((Math.random() * bag.length))
    }
    
    tempBag.push(bag[next])
    output += bag[next]

  }

  return output

}

result = randomBag()
console.log(result)