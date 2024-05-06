#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_RECORDS 10

typedef struct {
    int id;
    int size;
    char *data;
} Record;

typedef struct {
    int version;
    int numRecords;
    Record records[MAX_RECORDS];
} Database;

int loadDatabase(const char *filename, Database *db);
void displayRecord(Record *record);

int main(int argc, char **argv) {
    if (argc < 2) {
        //Expects a text file e.g., input2.txt
        printf("Usage: %s <database file>\n", argv[0]);
        return 1;
    }

    Database db;
    if (loadDatabase(argv[1], &db) != 0) {
        printf("Failed to load database\n");
        return 1;
    }
    

    for (int i = 0; i < db.numRecords; i++) {
        displayRecord(&db.records[i]);
    }

    return 0; 
}

int loadDatabase(const char *filename, Database *db) {
    FILE *file = fopen(filename, "r");
    if (!file) {
        perror("Error opening file");
        return -1;
    }

    fscanf(file, "%d %d", &db->version, &db->numRecords);
    for (int i = 0; i < db->numRecords && i < MAX_RECORDS; i++) {
        fscanf(file, "%d %d", &db->records[i].id, &db->records[i].size);
        db->records[i].data = malloc(db->records[i].size * sizeof(char)); //10x1
        if (db->records[i].data == NULL) {
            perror("Failed to allocate memory for record data");
            fclose(file);
            return -1;
        }
        fread(db->records[i].data, sizeof(char), db->records[i].size, file);
        
    }
    
    fclose(file);
    return 0;
}

void displayRecord(Record *record) {
    printf("Record ID: %d\n", record->id);
    printf("Data: %s\n", record->data);
}
