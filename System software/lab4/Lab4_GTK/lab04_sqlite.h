#ifndef LAB04_SQLITE_H
#define LAB04_SQLITE_H

#define DB_FILE "5lab.db"

void sqlite_insert(char *klichka, char* date, char * pol, int vid_id, int korm_id);
void sqlite_delete(int);
void sqlite_get_data(int);
void sqlite_update(int animalid, char*klichka, char*date, char*pol, int vid_id, int korm_id);

#endif
