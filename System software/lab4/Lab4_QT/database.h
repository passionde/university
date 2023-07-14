#ifndef DATABASE_H
#define DATABASE_H

#include <QDate>
#include <QDebug>
#include <QFile>
#include <QObject>
#include <QSql>
#include <QSqlDatabase>
#include <QSqlError>
#include <QSqlQuery>

#define DATABASE_HOSTNAME "ExampleDataBase"
#define DATABASE_NAME "5lab.db"

#define TABLE_VID "Vid"
#define VID_ID "id"
#define VID_NAME "nazvanie"


#define TABLE_KORM "korm"
#define KORM_ID "id"
#define KORM_VID "vid"
#define KORM_IZG "izgotovitel"
#define KORM_NAME "nazvanie"
#define KORM_PRICE "price"


#define TABLE_ANIMAL "Animal"
#define ANIMAL_ID "id"
#define ANIMAL_KLICH "klichka"
#define ANIMAL_DATE "date_of_birth"
#define ANIMAL_NUM "num_pages"
#define ANIMAL_POL "pol"



class DataBase : public QObject
{
    Q_OBJECT
  public:
    explicit DataBase(QObject *parent = nullptr);
    ~DataBase();
    void connectToDataBase();
    bool inserIntoMainTable(const QVariantList &data);
    bool inserIntoDeviceTable(const QVariantList &data);

  private:
    QSqlDatabase db;

  private:
    bool openDataBase();
    bool restoreDataBase();
    void closeDataBase();
    bool createMainTable();
    bool createDeviceTable();
};

#endif   // DATABASE_H
