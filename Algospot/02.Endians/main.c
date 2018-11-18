#include<stdio.h>

int main() {
	int testNum;
	unsigned int input = 0, result = 0;
	unsigned int convertFunc(unsigned int);

	scanf("%d", &testNum);
	for (int i = 0; i < testNum; i++) {
		scanf("%u", &input);
		result = convertFunc(input);
		printf("%u\n", result);
	}
	return 0;
}

unsigned int convertFunc(unsigned int input) {
	unsigned int result = 0;
	unsigned char temp[4] = { 0, };
	
	for (int i = 0; i < 4; i++) {
		temp[i] = input >> (i*8);
	}
	result = temp[0] << 24 | temp[1] << 16 | temp[2] << 8 | temp[3];

	return result;
}