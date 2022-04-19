#include <stdio.h>
#include "main.h"

int main(void)
{
	int i = 25519;
	char * store;
	
	store = _itoa(i, char strings[], 10);
	
	printf("%s", store);
	return (0);
}

