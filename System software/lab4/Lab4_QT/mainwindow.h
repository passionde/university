#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "database.h"

#include <QMainWindow>
#include <QSqlRelation>
#include <QSqlRelationalDelegate>
#include <QSqlRelationalTableModel>

namespace Ui
{
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

  public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

  private slots:
    void on_checkBox_stateChanged(int state);

    void on_btnexit_clicked();

    void on_btnabout_clicked();

    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_tableView_clicked(const QModelIndex &index);

    void on_pushButton_3_clicked();

private:
    Ui::MainWindow *ui;
    DataBase *db;
    QSqlRelationalTableModel *model;
    int row;
  private:
    void setupModel(const QString &tableName, const QStringList &headers);
    void createUI();
};

#endif   // MAINWINDOW_H
