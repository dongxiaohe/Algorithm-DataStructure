const findIndices = (array, target) => {
   for (let i = 0; i < array.length; i ++) {
	for (let j = i + 1; j < array.length; j ++ ) {
		if (array[i] + array[j] == target) {
			return [i, j];
		}
	}
   }
   return [];
}
console.log(findIndices([2, 7, 11, 15], 9));
console.log(findIndices([2, 7, 11, 30], 37));
console.log(findIndices([2, 7, 11, 15, 30], 45));
console.log(findIndices([2, 7, 11, 15, 30], 100));