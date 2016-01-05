function palindrome(input) {
	var words = input.split("\n").slice(1).join('');
	var stripped = words.toLowerCase().replace(/[^a-z]/g, '')
	return stripped == stripped.split('').reverse().join('') ? "Palindrome" : "Not a palindrome"
}

console.log(palindrome("3\nWas it a car\nor a cat\nI saw?"))

console.log(palindrome("4\nA man, a plan, \na canal, a hedgehog, \na podiatrist, \nPanama!"))