#include <stdio.h>
#include <stdlib.h>

#include "stack.h"

void output_stack_state(STACK* src, STACK* aux, STACK* dest)	//	This is an illegal access to STACK datatype. Unadvised to replicate unless you know what you are doing.
{
	unsigned int i;
	printf("%5s%5s%5s\n", "src", "aux", "dest");
	for (i = src->size - 1; i != -1; i--)
	{
		printf("%5d%5d%5d\n", src->data[i], aux->data[i], dest->data[i]);
	}
	printf("---------------------------\n\n");
}

void move_disk(STACK* src, STACK* dest)	//	For readability purposes.
{
	int value = pop(src);	//	Pop is customized to clean up after itself.
	push(dest, value);
}

void toh(int disks, STACK* src, STACK* aux, STACK* dest)
{
	if (disks == 1)
	{
		output_stack_state(src, aux, dest);
		move_disk(src, dest);
	}
	else
	{
		toh(disks - 1, src, dest, aux);	//	Move all disks above self to aux.
		output_stack_state(src, aux, dest);
		move_disk(src, dest);			//	Move self.
		toh(disks - 1, aux, src, dest);	//	Get back all disks in aux.
	}
}

int main()
{
	STACK *src, *aux, *dest;
	unsigned int disks;

	printf("Enter the number of disks= ");
	scanf("%u", &disks);
	system("cls");

	if (disks == 0)	{	return 1;	}	//	Why would you ever do that?

	//	Prep:
	src = initialize_stack(disks);
	aux = initialize_stack(disks);
	dest = initialize_stack(disks);
	unsigned int i;
	for (i = disks; i != 0; i--)
	{
		//	Disks are represented as their size values.
		push(src, i);
	}

	//	Toh:
	toh(disks, src, aux, dest);

	// Output Final State:
	output_stack_state(src, aux, dest);

	//	Terminate:
	terminate_stack(src);
	terminate_stack(aux);
	terminate_stack(dest);
	system("pause");
	return 0;
}
