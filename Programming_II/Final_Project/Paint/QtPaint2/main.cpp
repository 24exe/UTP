#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    // The main application
    QApplication app(argc, argv);

    // Create and open the main window
    MainWindow window;
    window.show();

    // Display the main window
    return app.exec();
}
