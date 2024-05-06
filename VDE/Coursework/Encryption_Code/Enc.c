#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char plainText[32];  // Global fixed size plain text

void encrypt(char *text, int key)
{
    int i; // Counter
    char *cipherText; // Variable for dynamically allocated memory and storing cipher text
    
    strncpy(plainText, text, strlen(text));  // Assign text to plain text (If original text is longer than plainText, it's expected to overflow)

    cipherText = malloc(sizeof(plainText)+10);  // Creating dynamic memory (length of the plain text + 10 (42 bytes))
    
    strcpy(cipherText, plainText); // copy the plain text to the cipher text (strcpy(Dest,Src))

    for (i = 0; i < strlen(cipherText); i++) { // For loop based on each character in the cipher text

    //In this section it's expected that to get a heap overflow
        cipherText[i] = cipherText[i] + key; //
        
    }

    printf(cipherText); // Printing the cipher text - Used in format string vuln
    
    free(cipherText);  // Free the allocated memory
}
void printUnEncrypted(){
    printf("Encrypted Text: %s\n", plainText); //Unused function - Prints original plain text without decryption
}
int main(int argc, char **argv)
{
    char input[256]; // create input variable (Higher length than plainText)
    int num; // create num variable (for use with ceaser cipher key)

    printf("Enter your text: "); //Asks user for the text to encrypt
    scanf("%s", input); // Read the input

    printf("Enter a key: "); // Asks user for the key
    scanf("%d", &num); // Read the key
    printf("Text: %s\nKey: %d\n", input, num); // Printing the text and key on the same line

    encrypt(input, num); // Calling the encrypt function passing the text and key

    return 0; // Exiting the program
}

