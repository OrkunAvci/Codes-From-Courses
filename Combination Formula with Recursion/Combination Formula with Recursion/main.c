#include <stdio.h>
#include <stdlib.h>

/*
	Disclaimer:
		The logic behind the actions taken here comes from Pascal's triangle.
		As math: C(n)(r) = C(n-1)(r-1) + C(n-1)(r);
		Where n is the size of sample space and r is the request.
*/

int combination(int n, int r)
{
	//	If most (Left side or Right side) of the triangle.
	if (r == 0 || r == n)
	{
		return 1;
	}
	return combination(n - 1, r - 1) + combination(n - 1, r);
}

int main()
{
	int n, r;

	printf("Enter the size of sample space: ");
	scanf("%d", &n);

	printf("Enter the number of requested elements: ");
	scanf("%d", &r);
	system("cls");

	if (n < r)
	{
		printf("Invalid input.");
		return 0;
	}

	printf("The combination is: %d", combination(n, r));

	system("pause");
	return 0;
}
