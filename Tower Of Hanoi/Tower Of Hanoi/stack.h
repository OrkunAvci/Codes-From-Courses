/*
	Taken from my library repository:
		Library / C / Datatype - Stack
*/
#ifndef STACK_H
#define STACK_H

typedef struct STACK
{
	unsigned int pointer;
	unsigned int size;
	int* data;
}STACK;

STACK* initialize_stack(unsigned int);	//	Takes stack and size, and allocates (data).
void terminate_stack(STACK*);					//	Deallocates (data) and resets other values.

int pop(STACK*);			//	Returns single value at (point -1).
void push(STACK*, int);		//	Stores single value at (point).

#endif
