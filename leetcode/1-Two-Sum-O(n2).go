package main;

import "fmt";

func main() {
	fmt.Println(findIndices([]int{2, 7, 11, 15}, 9));
	fmt.Println(findIndices([]int{2, 7, 11, 30}, 37));
	fmt.Println(findIndices([]int{2, 7, 11, 15}, 100));
}

func findIndices(array []int, target int) []int {
	length := len(array)
	for i := 0; i < length; i ++ {
		for j := i + 1; j < length; j ++ {
			if (array[i] + array[j] == target) {
				return []int{i, j};
			}
		}
	}
	return []int{};
}