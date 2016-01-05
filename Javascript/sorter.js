let sorter = words => {
  for (let entry of words) {
    (entry == entry.split('').sort().join('')) ? console.log(`${entry} is ordered`): console.log(`${entry} is not ordered`);
    (entry.split('').reverse().join('') == entry.split('').reverse().sort().join('')) ? console.log(`${entry} is ordered when reversed`): console.log(`${entry} is not ordered when reversed`);
  }
}

sorter(['almost', 'there'])