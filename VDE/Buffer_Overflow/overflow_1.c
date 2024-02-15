#include <stdio.h>

void func2() {

    	printf( "This in func2\n" );
}

void func1( int a, int b ) {

    	int i = 3 ;
    	func2() ;
    	printf( "This is in func1\n" ) ;
}

int main() {

    	int a = 1 ;
    	int b = 2 ;
    	func1( a, b ) ;
    	printf( "End of demo\n"  );
    	return 0;

}