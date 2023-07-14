#include <sqlite3.h>
#include <stdio.h>
#include "lab04_sqlite.h"

int callback(void *, int, char **, char **);
void sqlite_get_data(int flag)
{
    sqlite3 *db;
    char *err_msg = 0;
    int rc;
    if (SQLITE_OK != (rc = sqlite3_open(DB_FILE, &db)))
    {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
    }

    char sql[512]; 
     sprintf(sql, "SELECT Animal.id, Animal.klichka, Animal.date_of_birth, Animal.pol, Vid.id, Vid.nazvanie,  \
                  korm.id, \
                  korm.vid \
              FROM \
                  ((Animal \
              INNER JOIN Vid ON Animal.vid_id =  Vid.id) \
              INNER JOIN korm ON Animal.korm_id = korm.id) WHERE Animal.hidden != %d;", flag);
    rc = sqlite3_exec(db, sql, callback, NULL, &err_msg);
    if (rc != SQLITE_OK)
    {
        fprintf(stderr, "Failed to select data\n");
        fprintf(stderr, "SQLite error: %s\n", err_msg);
        sqlite3_free(err_msg);
        sqlite3_close(db);
    }
    sqlite3_close(db);
}

void sqlite_insert(char *klichka, char* date, char * pol, int vid_id, int korm_id)
{
    sqlite3 *db;
    char *err_msg = 0;
    int rc;
    if (SQLITE_OK != (rc = sqlite3_open(DB_FILE, &db)))
    {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
    }

    char sql[256];
    sprintf(sql, "INSERT INTO Animal (klichka, date_of_birth, pol, vid_id, korm_id, hidden) VALUES ('%s', '%s', '%s', %d, %d, %d);", klichka, date, pol, vid_id, korm_id, 0);
    rc = sqlite3_exec(db, sql, callback, NULL, &err_msg);
    if (rc != SQLITE_OK)
    {
        fprintf(stderr, "Failed to select data\n");
        fprintf(stderr, "SQLite error: %s\n", err_msg);
        sqlite3_free(err_msg);
        sqlite3_close(db);
    }
    sqlite3_close(db);
}

void sqlite_delete(int animalid)
{
    sqlite3 *db;
    char *err_msg = 0;
    int rc;
    if (SQLITE_OK != (rc = sqlite3_open(DB_FILE, &db)))
    {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
    }

    char sql[256];
    sprintf(sql, "UPDATE Animal SET hidden = %d WHERE id = %d;", 1, animalid);
    rc = sqlite3_exec(db, sql, callback, NULL, &err_msg);
    if (rc != SQLITE_OK)
    {
        fprintf(stderr, "Failed to select data\n");
        fprintf(stderr, "SQLite error: %s\n", err_msg);
        sqlite3_free(err_msg);
        sqlite3_close(db);
    }
    sqlite3_close(db);
}

void sqlite_update(int animalid, char*klichka, char*date, char*pol, int vid_id, int korm_id)
{
    sqlite3 *db;
    char *err_msg = 0;
    int rc;
    if (SQLITE_OK != (rc = sqlite3_open(DB_FILE, &db)))
    {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
        sqlite3_close(db);
    }


    char sql_comp[255];
    sprintf(sql_comp, "UPDATE Animal SET klichka = '%s', date_of_birth = '%s', pol = '%s', vid_id = %d, korm_id = %d WHERE id = %d;", klichka, date, pol, vid_id, korm_id, animalid);
    rc = sqlite3_exec(db, sql_comp, NULL, NULL, &err_msg);
    if (rc != SQLITE_OK)
    {
        fprintf(stderr, "Failed to update data in components\n");
        fprintf(stderr, "SQLite error: %s\n", err_msg);
        sqlite3_free(err_msg);
        sqlite3_close(db);
    }
    sqlite3_close(db);
}
