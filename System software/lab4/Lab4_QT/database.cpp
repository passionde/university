#include "database.h"

DataBase::DataBase(QObject *parent) : QObject(parent)
{
}

DataBase::~DataBase()
{
}

void DataBase::connectToDataBase()
{
    if (QFile("5lab.db").exists())
    {
        this->openDataBase();
    }
}

bool DataBase::openDataBase()
{
    db = QSqlDatabase::addDatabase("QSQLITE");
    //db.setHostName(DATABASE_HOSTNAME);
    db.setDatabaseName("5lab.db");
    if (db.open())
    {
        return true;
    }
    else
    {
        qDebug() << "Cannot open database: " << db.lastError().text();
        db.close();
        return false;
    }
}

void DataBase::closeDataBase()
{
    db.close();
}
