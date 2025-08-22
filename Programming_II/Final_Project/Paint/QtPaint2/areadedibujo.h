#ifndef AREADEDIBUJO_H
#define AREADEDIBUJO_H
#include <QColor>
#include <QImage>
#include <QPoint>
#include <QWidget>
class AreaDeDibujo : public QWidget
{
    Q_OBJECT

public:
    enum Herramienta{Lapiz, Borrador, Rectangulo, Circulo, Triangulo, Linea};

    AreaDeDibujo(QWidget *parent = 0);

    bool abrirImagen(const QString &nombreArchivo);
    bool guardarImagen(const QString &nombreArchivo, const char *formatoArchivo);
    void establecerColorDeLapiz(const QColor &nuevoColor);
    void establecerTamañoDeLapiz(int nuevoTamaño);
    void establecerHerramienta(Herramienta nuevaHerramienta);
    bool haSidoMoficada() const { return modificada; }
    QColor colorDeLapiz() const { return miColorDeLapiz; }
    int penWidth() const { return miTamañoDeLapiz; }

public slots:

    void limpiarImagen();
    void usarBorrador();

protected:
    void mousePressEvent(QMouseEvent *event) override;
    void mouseMoveEvent(QMouseEvent *event) override;
    void mouseReleaseEvent(QMouseEvent *event) override;
    void paintEvent(QPaintEvent *event) override;
    void resizeEvent(QResizeEvent *event) override;

private:
    void trazarLinea(const QPoint &puntoFinal);

    void dibujarRectangulo(const QPoint &puntoFinal);
    void dibujarCirculo(const QPoint &puntoFinal);
    void dibujarTriangulo(const QPoint &puntoFinal);
    void dibujarLinea(const QPoint &puntoFinal);

    void tamañoDeLaImagen(QImage *imagen, const QSize &tamañoNuevo);

    bool modificada;
    bool garabatos;
    int miTamañoDeLapiz;

    QColor miColorDeLapiz;
    QImage imagen;
    QPoint ultimoPunto;
    QPoint puntoInicial;
    Herramienta herramientaActual;
};

#endif
