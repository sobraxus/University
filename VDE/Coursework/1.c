#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[64];
    void (*printName)();
} User;

void printUserName() {
    printf("This function should not be accessible directly.\n");
}

User* createUser(const char* name) {
    User *user = malloc(sizeof(User));
    if (user) {
        strncpy(user->name, name, sizeof(user->name) - 1);
        user->name[sizeof(user->name) - 1] = '\0';
        user->printName = NULL;
    }
    return user;
}

void editUser(User *user, const char* newName) {
    strncpy(user->name, newName, strlen(newName) + 1);
}

void deleteUser(User **user) {
    free(*user);
    *user = NULL;
}

int main(int argc, char **argv) {
    char input[128];
    unsigned int index;
    User *users[2];

    printf("Creating users...\n");
    users[0] = createUser("User1");
    users[1] = createUser("Default User");

    printf("Enter user index to edit (0-1): ");
    scanf("%u", &index);
    printf("Enter new name: ");
    scanf("%s", input);

    if (index < 2) {
        editUser(users[index], input);
    } else {
        printf("Invalid index\n");
        return 1;
    }

    printf("User %u name changed to %s\n", index, users[index]->name);

    
    printf("Deleting user 0...\n");
    deleteUser(&users[0]);

   
    printf("Enter a format string: ");
    scanf("%s", input);
    printf(input);
    printf("\n");

    return 0;
}
