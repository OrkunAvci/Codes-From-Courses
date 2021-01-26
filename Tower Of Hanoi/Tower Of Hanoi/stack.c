#include "stack.h"

STACK* initialize_stack(unsigned int size)
{
	STACK* st = (STACK*) calloc(1, sizeof(STACK));
	st->pointer = 0;
	st->size = size;
	st->data = (int*) calloc(size, sizeof(int));
	return st;
}

void terminate_stack(STACK* st)
{
	free(st->data);
	free(st);
}

int pop(STACK* st)	//	Customized.
{
	if (st->pointer == 0) { return	-1; }	//	Configure to an impossible value.

	//	Store to return and reset the cell.
	st->pointer--;
	int value = st->data[st->pointer];
	st->data[st->pointer] = 0;

	return value;
}

void push(STACK* st, int addon)
{
	if (st->pointer == st->size) { return; }
	st->data[st->pointer] = addon;
	st->pointer++;
}
