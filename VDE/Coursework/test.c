#include <stdio.h>
#include <stdlib.h>

typedef struct {
    char name[64];
    void (*printName)();
} User;

int main() {
    printf("Size of User struct: %zu bytes\n", sizeof(User));
    return 0;
}
