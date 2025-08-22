#include <QtWidgets>
#include "mainwindow.h"
#include "areadedibujo.h"

MainWindow::MainWindow()
{
    pinImagen = new AreaDeDibujo;
    setCentralWidget(pinImagen);

    crearAcciones();
    crearMenus();

    setWindowTitle(tr("Editor de dibujo"));
    resize(600, 600);
}

void MainWindow::closeEvent(QCloseEvent *event)
{
    if (talvezSalvar()) {
        event->accept();
    } else {
        event->ignore();
    }
}

void MainWindow::abrir()
{
    if (talvezSalvar()) {
        QString nombreArchivo = QFileDialog::getOpenFileName(this,
                                                             tr("Abrir Archivo"), QDir::currentPath());
        if (!nombreArchivo.isEmpty())
            pinImagen->abrirImagen(nombreArchivo);
    }
}

void MainWindow::guardar()
{
    QAction *action = qobject_cast<QAction *>(sender());

    QByteArray formatoArchivo = action->data().toByteArray();
    guardarArchivo(formatoArchivo);
}

void MainWindow::colorDeLapiz()
{
    QColor nuevoColor = QColorDialog::getColor(pinImagen->colorDeLapiz());

    if (nuevoColor.isValid())
        pinImagen->establecerColorDeLapiz(nuevoColor);
}

void MainWindow::penWidth()
{
    bool ok;
    int nuevoTamaño = QInputDialog::getInt(this, tr("Editor de dibujo"),
                                           tr("Selecciona el tamaño :"),
                                           pinImagen->penWidth(),
                                           1, 50, 1, &ok);
    if (ok)
        pinImagen->establecerTamañoDeLapiz(nuevoTamaño);
}

void MainWindow::crearAcciones()
{
    accionAbrir = new QAction(tr("&Abrir..."), this);
    accionAbrir->setShortcuts(QKeySequence::Open);

    connect(accionAbrir, SIGNAL(triggered()), this, SLOT(abrir()));

    QStringList formatosPermitidos;
    formatosPermitidos<< "PNG" <<"JPG"<< "TIFF"<< "BMP";

    foreach (const QString &formato, formatosPermitidos) {
        QString text = tr("%1...").arg(formato);
        QAction *action = new QAction(text, this);

        action->setData(QByteArray(formato.toLatin1()));
        connect(action, SIGNAL(triggered()), this, SLOT(guardar()));

        accionesGuardarComo.append(action);
    }

    ;
    accionDeSalir = new QAction(tr("&Salir"), this);
    accionDeSalir->setShortcuts(QKeySequence::Quit);
    connect(accionDeSalir, SIGNAL(triggered()), this, SLOT(close()));

    actColorLapiz = new QAction(tr("&Color de lapiz..."), this);
    connect(actColorLapiz, SIGNAL(triggered()), this, SLOT(colorDeLapiz()));

    penWidthAct = new QAction(tr("&Tamaño de lapiz..."), this);
    connect(penWidthAct, SIGNAL(triggered()), this, SLOT(penWidth()));

    actBorrador = new QAction(tr("&Borrador"), this);
    connect(actBorrador, SIGNAL(triggered()), this, SLOT(usarBorrador()));

    actLimpiarPantalla = new QAction(tr("&Limpiar pantalla"), this);
    actLimpiarPantalla->setShortcut(tr("Ctrl+L"));
    connect(actLimpiarPantalla, SIGNAL(triggered()),
            pinImagen, SLOT(limpiarImagen()));

    actLapiz = new QAction(tr("&Lapiz"), this);
    connect(actLapiz, SIGNAL(triggered()), this, SLOT(seleccionarLapiz()));

    actRectangulo = new QAction(tr("&Rectángulo"), this);
    connect(actRectangulo, SIGNAL(triggered()), this, SLOT(seleccionarRectangulo()));

    actCirculo = new QAction(tr("&Círculo"), this);
    connect(actCirculo, SIGNAL(triggered()), this, SLOT(seleccionarCirculo()));

    actTriangulo = new QAction(tr("&Triángulo"), this);
    connect(actTriangulo, SIGNAL(triggered()), this, SLOT(seleccionarTriangulo()));

    actLinea = new QAction(tr("&Línea"), this);
    connect(actLinea, SIGNAL(triggered()), this, SLOT(seleccionarLinea()));
}

void MainWindow::crearMenus()
{
    menuGuardarComo = new QMenu(tr("&Guardar como: "), this);

    foreach (QAction *action, accionesGuardarComo)
        menuGuardarComo->addAction(action);

    menuArchivo = new QMenu(tr("&Archivo"), this);
    menuArchivo->addAction(accionAbrir);
    menuArchivo->addMenu(menuGuardarComo);
    menuArchivo->addSeparator();
    menuArchivo->addAction(accionDeSalir);

    menuOpciones = new QMenu(tr("&Opciones"), this);
    menuOpciones->addAction(actColorLapiz);
    menuOpciones->addAction(penWidthAct);
    menuOpciones->addSeparator();
    menuOpciones->addAction(actLimpiarPantalla);

    lapiz = new QMenu(tr("&Lapiz"),this);
    lapiz->addAction(actLapiz);

    borrador = new QMenu(tr("Borrador"),this);
    borrador->addAction(actBorrador);

    menuFiguras = new QMenu (tr("&Figuras"), this);
    menuFiguras->addAction(actRectangulo);
    menuFiguras->addAction(actCirculo);
    menuFiguras->addAction(actTriangulo);
    menuFiguras->addAction(actLinea);

    menuBar()->addMenu(menuArchivo);
    menuBar()->addMenu(menuOpciones);
    menuBar()->addMenu(lapiz);
    menuBar()->addMenu(borrador);
    menuBar()->addMenu(menuFiguras);

}

void MainWindow::usarBorrador()
{
    pinImagen->establecerHerramienta(AreaDeDibujo::Borrador);
    pinImagen->establecerColorDeLapiz(Qt::white);
}

void MainWindow::seleccionarLapiz()
{
    pinImagen->establecerHerramienta(AreaDeDibujo::Lapiz);
    pinImagen->establecerColorDeLapiz(Qt::blue);
}

void MainWindow::seleccionarRectangulo()
{
    pinImagen->establecerHerramienta(AreaDeDibujo::Rectangulo);
    pinImagen->establecerColorDeLapiz(Qt::blue);
}

void MainWindow::seleccionarCirculo()
{
    pinImagen->establecerHerramienta(AreaDeDibujo::Circulo);
    pinImagen->establecerColorDeLapiz(Qt::blue);
}

void MainWindow::seleccionarTriangulo()
{
    pinImagen->establecerHerramienta(AreaDeDibujo::Triangulo);
    pinImagen->establecerColorDeLapiz(Qt::blue);
}

void MainWindow::seleccionarLinea()
{
    pinImagen->establecerHerramienta(AreaDeDibujo::Linea);
    pinImagen->establecerColorDeLapiz(Qt::blue);
}

bool MainWindow::talvezSalvar()
{
    if (pinImagen->haSidoMoficada()) {
        QMessageBox::StandardButton ret;
        ret = QMessageBox::warning(this, tr("Editor de dibujo"),
                                   tr("La imagen ha sido modificada.\n"
                                      "¿Quieres guardar los cambios?"),
                                   QMessageBox::Save | QMessageBox::Discard
                                       | QMessageBox::Cancel);
        if (ret == QMessageBox::Save) {
            return guardarArchivo("png");
        } else if (ret == QMessageBox::Cancel) {
            return false;
        }
    }
    return true;
}

bool MainWindow::guardarArchivo(const QByteArray &formatoArchivo)
{
    QString initialPath = QDir::currentPath() + "/Sin titulo." + formatoArchivo;
    QString nombreArchivo = QFileDialog::getSaveFileName(this, tr("Save As"),
                                                         initialPath,
                                                         tr("%1 Files (.%2);;All Files ()")
                                                             .arg(QString::fromLatin1(formatoArchivo.toUpper()))
                                                             .arg(QString::fromLatin1(formatoArchivo)));
    if (nombreArchivo.isEmpty()) {
        return false;
    } else {
        return pinImagen->guardarImagen(nombreArchivo, formatoArchivo.constData());
    }
}
