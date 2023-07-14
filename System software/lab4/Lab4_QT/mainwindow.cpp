#include "mainwindow.h"

#include "ui_mainwindow.h"

#include <QMessageBox>
#include <QSqlRecord>

int flag = 0;

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    db = new DataBase();
    db->connectToDataBase();
    this->setupModel(TABLE_ANIMAL, QStringList() << "id животного"
                                               << "Кличка"
                                               << "Дата рождения"
                                               << "Пол"
                                               << "Вид"
                                               << "Корм");
    this->createUI();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::setupModel(const QString &tableName, const QStringList &headers)
{

    model = new QSqlRelationalTableModel(this);
    model->setTable(tableName);
    model->setRelation(4, QSqlRelation(TABLE_VID, VID_ID, VID_NAME));
    model->setRelation(5, QSqlRelation(TABLE_KORM, KORM_ID, KORM_NAME));
    //model->setRelation(6, QSqlRelation(TABLE_KORM, KORM_ID, KORM_IZG));
    //model->setRelation(7, QSqlRelation(TABLE_KORM, KORM_ID, KORM_PRICE));
    for (int i = 0, j = 0; i < model->columnCount() - 1; i++, j++)
    {
        model->setHeaderData(i, Qt::Horizontal, headers[j]);
    }
    model->select();
}

void MainWindow::createUI()
{
    model->setFilter(QString("hidden = 0"));
    ui->tableView->setModel(model);
    ui->tableView->setColumnHidden(0, true);
    ui->tableView->setColumnHidden(6, true);
    ui->tableView->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->tableView->setSelectionMode(QAbstractItemView::SingleSelection);
    ui->tableView->resizeColumnsToContents();
    ui->tableView->setItemDelegate(new QSqlRelationalDelegate(ui->tableView));
    ui->tableView->horizontalHeader()->setStretchLastSection(true);
    model->select();
}

void MainWindow::on_checkBox_stateChanged(int state)
{
    flag ^= 1;
    model->setFilter(QString("hidden = '%1'")
                         .arg(flag));
    ui->tableView->setModel(model);
    ui->tableView->setColumnHidden(0, true);
    ui->tableView->setColumnHidden(6, true);
    ui->tableView->setSelectionBehavior(QAbstractItemView::SelectRows);
    ui->tableView->setSelectionMode(QAbstractItemView::SingleSelection);
    ui->tableView->resizeColumnsToContents();
    ui->tableView->setItemDelegate(new QSqlRelationalDelegate(ui->tableView));
    ui->tableView->horizontalHeader()->setStretchLastSection(true);
    model->select();
}

void MainWindow::on_btnexit_clicked()
{
    this->close();
}

void MainWindow::on_btnabout_clicked()
{
    QMessageBox msgBox;
    msgBox.information(this, "О программе", "Это как ваша лабораторная работа №4, только меньше");
}

void MainWindow::on_pushButton_clicked()
{
    model->insertRow(model->rowCount());

}


void MainWindow::on_pushButton_2_clicked()
{
    QSqlRecord rec = model->record(row);
    rec.setValue("hidden", 1);
    model->setRecord(row, rec);
    createUI();
}


void MainWindow::on_tableView_clicked(const QModelIndex &index)
{
    row = index.row();
}


void MainWindow::on_pushButton_3_clicked()
{
    createUI();
}

