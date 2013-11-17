template <class T>
// arr - searching list
// len - length of the list
// what - searching element
int binSearch(const T arr[], int len, T what) {
	int low = 0;
	int high = len - 1;
	while (low <= high) {
		int mid = (low + high) / 2;
		if (arr[mid] > what)
			high = mid - 1;
		else if (arr[mid] < what)
			low = mid + 1;
		else
			return mid;
	}
	return -1;
}

// test drive
#include <iostream>

int main() {
	int array[] = {2, 3, 5, 6, 8};
	int result1 = binSearch(array, sizeof(array)/sizeof(int), 4);
	int result2 = binSearch(array, sizeof(array)/sizeof(int), 8);

	if (result1 == -1) 
	 	std::cout << "4 not found!" << std::endl;
  	else 
  		std::cout << "4 found at " << result1 << std::endl;

  	if (result2 == -1) 
  		std::cout << "8 not found!" << std::endl;
  	else 
  		std::cout << "8 found at " << result2 << std::endl;

  	return 0;
}