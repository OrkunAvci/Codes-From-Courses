#include <stdio.h>
#include <stdlib.h>

int fib(int* arr, int n)
{
	if (n < 2)
	{
		return n;
	}
	
	if (arr[n - 1] == -1)
	{
		arr[n - 1] = fib(arr, n - 1);
	}
	if (arr[n - 2] == -1)
	{
		arr[n - 2] = fib(arr, n - 2);
	}

	return arr[n - 1] + arr[n - 2];
}

int* innitialize(int n)
{
	if (n < 1)
	{
		return NULL;
	}

	int* arr = (int*) calloc(n, sizeof(int));
	
	int i;
	for (i = 0; i < n; i++)
	{
		arr[i] = -1;
	}

	return arr;
}

int main()
{
	int n;
	printf("Give me a n:");
	scanf("%d", &n);
	system("cls");

	int* arr = innitialize(n);
	if (arr == NULL)
	{
		printf("Invalid input. \nTerminated...\n\n");
		return 0;	//	Customize this value to your needs.
	}

	int answer = fib(arr, n);

	printf("The answer for Fib(%d) is: %d\n\n", n, answer);

	system("pause");
	free(arr);
	return 0;
}