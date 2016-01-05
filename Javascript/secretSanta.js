function secretSanta(input) {
  var allData = input.split('\n')
  var nonMixers = []
  for (var i = 0; i < allData.length; i++) {
    if (allData[i].match(/\s/)) {
    	console.log(allData[i])
      splitData = allData[i].split(' ')
      console.log(splitData)
      for (var j = 0; j <= splitData.length; j++) {
        nonMixers.push(splitData[j])
      };
    }
  };

  console.log(nonMixers)


}
secretSanta("Sean\nWinnie\nBrian Amy\nSamir\nJoe Bethany\nBruno Anna Matthew Lucas\nGabriel Martha Philip\nAndre\nDanielle\nLeo Cinthia\nPaula\nMary Jane\nAnderson\nPriscilla\nRegis Julianna Arthur\nMark Marina\nAlex Andrea")