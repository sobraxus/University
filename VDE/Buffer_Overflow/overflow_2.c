#include <stdio.h>
#include <stdlib.h>
#include <io.h>

int main(int argc, char *argv[]) {

    	volatile int modified ; //indicates variable may change between accesses
    	char buffer[16] ; //8 bytes
    	modified = 0 ;

    	strcpy( buffer, argv[1] ) ; //copy arg[1] into buffer

    	if(modified != 0) {
      	printf("The 'modified' variable has changed. Well done!\n");
    	}
    	else {
      	printf("Try again\n");
    	}

    	return 0 ;

}