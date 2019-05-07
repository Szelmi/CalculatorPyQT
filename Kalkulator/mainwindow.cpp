#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    player = new QMediaPlayer(this);

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    player -> setMedia(QUrl::fromLocalFile("C:\\Users\\Mateusz\\Desktop\\QT\\Kalkulator\\voice.wav"));
    player -> play();
    qDebug() << player->errorString();
}

void MainWindow::on_pushButton_10_clicked()
{
    player -> stop();
}
