#include <QtWidgets>
#if defined(QT_PRINTSUPPORT_LIB)
#include <QtPrintSupport/qtprintsupportglobal.h>
#if QT_CONFIG(printdialog)
#include <QPrinter>
#include <QPrintDialog>
#endif
#endif

#include "areadedibujo.h"

AreaDeDibujo::AreaDeDibujo(QWidget *parent)
    : QWidget(parent)
{
    setAttribute(Qt::WA_StaticContents);

    modificada = false;
    garabatos = false;
    miTamañoDeLapiz = 1;
    miColorDeLapiz = Qt::blue;
    herramientaActual = Lapiz;
}


bool AreaDeDibujo::abrirImagen(const QString &nombreArchivo)
{
    QImage imagenCargada; // Esta variable se utiliza para cargar la imagen desde el archivo especificado por nombreArchivo

    if (!imagenCargada.load(nombreArchivo))
        return false;

    QSize tamañoNuevo = imagenCargada.size().expandedTo(size());
    tamañoDeLaImagen(&imagenCargada, tamañoNuevo);
    imagen = imagenCargada;
    modificada = false;
    update();
    return true;
}

bool AreaDeDibujo::guardarImagen(const QString &nombreArchivo, const char *formatoArchivo)
{
    QImage imagenVisible = imagen;
    tamañoDeLaImagen(&imagenVisible, size());

    if (imagenVisible.save(nombreArchivo, formatoArchivo)) {
        modificada = false;
        return true;
    } else {
        return false;
    }
}

void AreaDeDibujo::establecerColorDeLapiz(const QColor &nuevoColor)
{
    miColorDeLapiz = nuevoColor;
}

void AreaDeDibujo::establecerTamañoDeLapiz(int nuevoTamaño)
{
    miTamañoDeLapiz = nuevoTamaño;
}

void AreaDeDibujo::establecerHerramienta(Herramienta nuevaHerramienta){
    herramientaActual = nuevaHerramienta;
}

void AreaDeDibujo::limpiarImagen()
{
    imagen.fill(qRgb(255, 255, 255));
    modificada = true;
    update();
}

void AreaDeDibujo::mousePressEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton) {
        ultimoPunto = event->pos();
        puntoInicial = event->pos();
        garabatos = true;
    }
}

void AreaDeDibujo::mouseMoveEvent(QMouseEvent *event)
{
    if ((event->buttons() & Qt::LeftButton) && garabatos) {
        switch (herramientaActual) {
        case Lapiz:
        case Borrador:
            trazarLinea(event->pos());
            break;
        case Rectangulo:
        case Circulo:
        case Triangulo:
        case Linea:
            update();
            break;
        }
    }
}

void AreaDeDibujo::mouseReleaseEvent(QMouseEvent *event)
{
    if (event->button() == Qt::LeftButton && garabatos) {
        switch (herramientaActual) {
        case Lapiz:
        case Borrador:
            trazarLinea(event->pos());
            break;
        case Rectangulo:
            dibujarRectangulo(event->pos());
            break;
        case Circulo:
            dibujarCirculo(event->pos());
            break;
        case Triangulo:
            dibujarTriangulo(event->pos());
            break;
        case Linea:
            dibujarLinea(event->pos());
            break;
        }
        garabatos = false;
    }
}

void AreaDeDibujo::paintEvent(QPaintEvent *event)
{
    QPainter painter(this);
    QRect dirtyRect = event->rect();
    painter.drawImage(dirtyRect, imagen, dirtyRect);

    QPointF points[3];

    if (garabatos && (herramientaActual == Rectangulo || herramientaActual == Circulo || herramientaActual == Triangulo || herramientaActual == Linea)) {
        painter.setPen(QPen(miColorDeLapiz, miTamañoDeLapiz, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
        switch (herramientaActual) {
        case Rectangulo:
            painter.drawRect(QRect(puntoInicial, ultimoPunto));
            break;
        case Circulo:
            painter.drawEllipse(QRect(puntoInicial, ultimoPunto));
            break;
        case Triangulo:
            points[0] = QPointF(puntoInicial.x(), ultimoPunto.y());
            points[1] = QPointF((puntoInicial.x() + ultimoPunto.x()) / 2, puntoInicial.y());
            points[2] = QPointF(ultimoPunto.x(), ultimoPunto.y());
            painter.drawPolygon(points, 3);
            break;
        case Linea:
            painter.drawLine(puntoInicial, ultimoPunto);
            break;
        default:
            break;
        }
    }
}

void AreaDeDibujo::resizeEvent(QResizeEvent *event)
{
    if (width() > imagen.width() || height() > imagen.height()) {
        int nuevoTamaño = qMax(width() + 128, imagen.width());
        int newHeight = qMax(height() + 128, imagen.height());
        tamañoDeLaImagen(&imagen, QSize(nuevoTamaño, newHeight));
        update();
    }
    QWidget::resizeEvent(event);
}

void AreaDeDibujo::trazarLinea(const QPoint &puntoFinal)
{
    QPainter painter(&imagen);

    painter.setPen(QPen(miColorDeLapiz, miTamañoDeLapiz, Qt::SolidLine, Qt::RoundCap,
                        Qt::RoundJoin));

    painter.drawLine(ultimoPunto, puntoFinal);
    modificada = true;

    int rad = (miTamañoDeLapiz / 2) + 2;

    update(QRect(ultimoPunto, puntoFinal).normalized()
               .adjusted(-rad, -rad, +rad, +rad));

    ultimoPunto = puntoFinal;
}

void AreaDeDibujo::dibujarRectangulo(const QPoint &puntoFinal)
{
    QPainter painter(&imagen);
    painter.setPen(QPen(miColorDeLapiz, miTamañoDeLapiz, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
    painter.drawRect(QRect(puntoInicial, puntoFinal));
    modificada = true;
    update();
}

void AreaDeDibujo::dibujarCirculo(const QPoint &puntoFinal)
{
    QPainter painter(&imagen);
    painter.setPen(QPen(miColorDeLapiz, miTamañoDeLapiz, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
    painter.drawEllipse(QRect(puntoInicial, puntoFinal));
    modificada = true;
    update();
}

void AreaDeDibujo::dibujarTriangulo(const QPoint &puntoFinal)
{
    QPainter painter(&imagen);
    painter.setPen(QPen(miColorDeLapiz, miTamañoDeLapiz, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
    QPointF points[3] = {
        QPointF(puntoInicial.x(), puntoFinal.y()),
        QPointF((puntoInicial.x() + puntoFinal.x()) / 2, puntoInicial.y()),
        QPointF(puntoFinal.x(), puntoFinal.y())
    };
    painter.drawPolygon(points, 3);
    modificada = true;
    update();
}

void AreaDeDibujo::dibujarLinea(const QPoint &puntoFinal)
{
    QPainter painter(&imagen);
    painter.setPen(QPen(miColorDeLapiz, miTamañoDeLapiz, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin));
    painter.drawLine(puntoInicial, puntoFinal);
    modificada = true;
    update();
}

void AreaDeDibujo::tamañoDeLaImagen(QImage *imagen, const QSize &tamañoNuevo)
{
    if (imagen->size() == tamañoNuevo)
        return;

    QImage newImage(tamañoNuevo, QImage::Format_RGB32);
    newImage.fill(qRgb(255, 255, 255));

    QPainter painter(&newImage);
    painter.drawImage(QPoint(0, 0), *imagen);
    *imagen = newImage;
}
void AreaDeDibujo::usarBorrador()
{
    establecerColorDeLapiz(Qt::white);
}
