#include <stdio.h>
#include <string.h>

#define MAX_SIZE 32 //Global variable for maximum size
int i; // Counter variable
char stackBuffer[MAX_SIZE];  // Fixed-size buffer according to MAX_SIZE
char *heapBuffer; // Dynamically allocated memory

void encrypt(char *text, int key)
{
    strcpy(stackBuffer, text);  // Assign text to stack buffer (If text is longer than MAX_SIZE, it's expected to overflow)

    heapBuffer = malloc(strlen(stackBuffer) + 1);  // Creating dynamic memory (length of the stack buffer + 10 (138 bytes))
    
    strcpy(heapBuffer, stackBuffer); // copy the stack buffer to the heap buffer (strcpy(Dest,Src))

    for(i = 0; i < strlen(heapBuffer); i++) { // For loop based on each character in the heap buffer
    //In this section it's expected that to get a heap overflow
        heapBuffer[i] = heapBuffer[i] + key; //
    }
    
    printf(heapBuffer); // Printing the heap buffer

    free(heapBuffer);  // Free the allocated memory
}
void printUnEncrypted(){
    printf("Encrypted Text: %s\n", stackBuffer);
}
int main(int argc, char **argv)
{
    char input[256];
    int num;

    printf("Enter your text: ");
    scanf("%s", input);

    printf("Enter a key: ");
    scanf("%d", &num);

    // print text and key on same line 
    printf("Text: %s\nKey: %d\n", input, num);

    encrypt(input, num);

    return 0;
}

