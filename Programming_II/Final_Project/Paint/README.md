# **Informe Técnico del Proyecto en el framework QT – Aplicativo tipo ‘Paint’.**


## **Integrantes del proyecto con sus respectivos códigos.**

•	Carlos Eduardo Grisales Restrepo	1055750849

•	Maycol Becerra Castro			1221714653

•	David Stiven Rivas Obando		1004685578 

•	Pablo León Rueda			1123890964

## **Aplciacion**
### ***Funciones que tiene la App***

1. Lapiz funcional.
2. Paleta de colores con código RGB.
3. Selección de color.
4. Borrador funcional.
5. Seleccion de distintas figuras:
   
   4.1 Circulos.
   
   4.2 Triangulos.
   
   4.3 Rectangulos.
   
6. Limpiado de Pantalla.
7. Guardado de archivos en distintos formatos.
8. Cargado de archivos.
9. Cambio de Resolución de Pantalla.

### ***Estructura de la App.*** 

La app consta de una carpeta que se divide en las siguientes sub carpetas:
1.	Headers donde se contienen las cabeceras ‘areadedibujo.h’ y ‘mainwindow.h’ 
2.	Sources donde están los archivos ‘.cpp’ tales como ‘main.cpp’, ‘areadedibujo.cpp’ y ‘mainwindow.cpp’ 
3.	Forms carpeta en la que se almacenan los archivos ‘.ui’.

En un proyecto de Qt en C++ la carpeta Forms es utilizada para almacenar los archivos de diseño de interfaz
gráfica creados con el Editor de Formularios Qt Designer. Estos archivos suelen contener la descripción visual
de la interfaz de usuario, incluyendo los widgets, su disposición, propiedades y señales asociadas.
4.	Y, por último, el archivo ‘.pro’. Es un archivo de configuración del proyecto. Se utiliza para especificar las
dependencias, configuraciones de compilación, enlazado de bibliotecas y otros detalles importantes para compilar y construir un proyecto.	

### ***Definiciones Extra*** 

**- Headers:**
Las cabeceras contienen las declaraciones de clases, funciones y variables que se utilizan en tu código. Proporcionan una interfaz para que otros archivos de código fuente puedan utilizar estas clases y funciones sin necesidad de conocer los detalles de su implementación. Las cabeceras son fundamentales para la modularidad y la reutilización de código en proyectos de C+

**- Sources:**
Los Sources contienen la implementación de las clases, funciones y variables declaradas en los archivos de cabecera (.h o .hpp). En esencia, los archivos de código fuente son donde escribes el código real para realizar las operaciones y definir el comportamiento de tu programa en un proyecto de C++.

### ***Contenidos*** 

**Headers**

   *mainwindow.h*

   En este archivo se encuentran las siguientes funciones y variables: 

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
         
      Widgets del menu
             QMenu *menuGuardarComo;
             QMenu *menuArchivo;
             QMenu *menuOpciones;
             QMenu *lapiz;
             QMenu *menuFiguras;
             QMenu *borrador;
             QAction *accionAbrir;
             
      Acciones QT
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
             
   *areadedibujo.h*
   
   En este archivo se encuentran las siguientes funciones y variables: 
      
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
**Sources**

   *main.cpp*
   
   Este archivo se encarga de:
   
   Iniciar la aplicación Qt: Incluye la creación de una instancia de QApplication, que maneja el ciclo de vida de la aplicación.
   Crear y mostrar la ventana principal: Instancia y muestra la ventana principal o el widget principal del proyecto.
   
   Entrar en el bucle de eventos: Llama a app.exec() para iniciar el bucle de eventos de Qt, que maneja la interacción del usuario y otros eventos.
   En resumen, main.cpp establece y ejecuta la aplicación Qt.

   *mainwindow.cpp*

   Este archivo es responsable de crear la ventana principal del aplicativo y de definir funciones como 
   'closeEvent', 'abrir', 'guardar', 'colorDeLapiz', 'penWidth' (tamaño del lápiz), 'crear acciones', crear los menús mediante la definición
   la función 'crearMenus' y definir las funciones para guardar archivos, evitar que el usuario cierre la aplicación sin antes guardar, definir figuras, lineas,
   seleccionar borrador y seleccionar lápiz.

   *areadedibujo.cpp*

   En este archivo se definen funciones que permiten: abrir imagenes, establecer cual sera el color del lápiz y su tamaño, establecer que tipo de herramienta
   usara el usuario, limpiar la pantalla, re dimensionar la pantalla, dibujar cualquiera de las 3 figuras, trazar lineas y cualquiera de los siguientes eventos QT:
   
   • mousePressEvent: Permite saber si se esta presionando el click izquiero y en base a eso guarda el primer punto en el que dibujo y traza un punto hasta el ultimo punto.
   
   • mouseMoveEvent: Permite saber si el mouse se esta moviendo y si este se hace mientras se esta presionando el click izquierdo, dibuja una linea, siempre y cuando la
   herramienta seleccionada sea el borrador o el lápiz. Si es cualquiera de las tres figuras seleccionables, se dicha figura desde el primer punto hasta el punto en el que se
   suelta el click.
   
   • mouseReleaseEvent: Evalua cuando se solto el click izquierdo y así envia la ultima posición a las funciones de lapiz y borrador, si es cualquiera de las figuras, 
   envia la última posición para que estas calculen el tamaño de la figura. 
   
   • paintEvent: permite que se cree el dibujo. 
   
   Si la herramienta seleccionada es 'Rectangulo', se entrega el punto inicial y el punto final, para que el rectangulo se 
   imprima acorde a esas dimensiones. 
   
   Si la herramienta seleccionada es 'Circulo', se entrega el punto inicial y el punto final para que se imprima una elipse acorde a estos dos 
   puntos. 
   
   Si la herramienta seleccionada es 'Triangulo', se entregan estos 3 puntos:
   1. Punto inicial en el eje x, punto final en el eje y.
   2. Punto inicial en el eje x, punto final en el eje x.
   3. Punto inicial en el eje y, punto final en el eje x.
      
   Y con estos 3 punto se crea imprime un poligono entre ellos.

   Si la herramienta seleccionada es una Linea, se traza esta misma entre el punto inicial y el punto final.
   
   
   
