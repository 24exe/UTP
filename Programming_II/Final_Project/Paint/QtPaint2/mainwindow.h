#ifndef MAINWINDOW_H
#define MAINWINDOW_H
#include <QList>
#include <QMainWindow>

class AreaDeDibujo;

class MainWindow : public QMainWindow
{
    Q_OBJECT
public:
    MainWindow();

protected:
    void closeEvent(QCloseEvent *event) override;

private slots:
    void abrir();
    void guardar();
    void colorDeLapiz();
    void penWidth();
    void usarBorrador();
    void seleccionarLapiz();
    void seleccionarRectangulo();
    void seleccionarCirculo();
    void seleccionarTriangulo();
    void seleccionarLinea();

private:
    void crearAcciones();
    void crearMenus();
    bool talvezSalvar();
    bool guardarArchivo(const QByteArray &formatoArchivo);

    AreaDeDibujo *pinImagen;
    //widgets de menu
    QMenu *menuGuardarComo;
    QMenu *menuArchivo;
    QMenu *menuOpciones;
    QMenu *lapiz;
    QMenu *menuFiguras;
    QMenu *borrador;
    QAction *accionAbrir;

    QList<QAction *> accionesGuardarComo;
    QAction *accionDeSalir;
    QAction *actColorLapiz;
    QAction *penWidthAct;
    QAction *actLimpiarPantalla;
    QAction *actBorrador;
    QAction *actLapiz;
    QAction *actFiguras;
    QAction *actRectangulo;
    QAction *actCirculo;
    QAction *actTriangulo;
    QAction *actLinea;
};

#endif
