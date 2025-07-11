#lang racket
;Contrato: Agenda Telefónica:
;Propósito: Almacenar registros de diferentes tantas personas como se quiera y poder consultarlos o buscar alguno en especifico.

;lista que luego sera llenada por los contactos que se quieran guardar
(define listaagenda '())
;estructura de la agenda que guarda los datos
(define-struct agenda (name cc address number))
;datos que seran reescritos para ser ingresados a la agenda posteriormente
(define namedatas "")
(define menucontroller 0)
(define datascontroller 0)
(define menudatascontroller 0)
(define name "")
(define cc "")
(define address "")
(define number "")


;Función que permite al usuario añadir nuevos contactos
(define (userdatas)
  (begin
    (newline)
    (displayln "MENÚ PARA AGREGAR NUEVOS DATOS DE CONTACTO: ")
    (newline)
    (displayln "Digite su nombre (entre comillas dobles): ")
    (set! name (read))
    (display "Digite su cédula (entre comillas dobles): ")
    (newline)
    (set! cc (read))
    (display "Digite su dirección (entre comillas dobles): ")
    (newline)
    (set! address (read))
    (display "Digite su número telefonico (entre comillas dobles): ")
    (newline)
    (set! number (read))
    (set! listaagenda (cons (make-agenda name cc address number)listaagenda))
    (newline)
    (displayln "Si desea agregar otro contacto marque 1, si desea volver al menú, marque 2:")
    (set! datascontroller (read))
    (cond
      ((= datascontroller 1) (userdatas))
      ((= datascontroller 2) (menu))
      (else(begin
             (displayln "ERROR,SE LE DEVOLVERA AL MENÚ")
             (menu)
             )))))

;Función encargada de mostrar todos los contactos guardados cuando se pidan
(define (showdatas x)
  (cond
    (( = x (length listaagenda)) (begin
                                   (newline)
                                   (displayln "FIN DE LOS CONTACTOS GUARDADOS, SE LE DEVOLVERA AL MENÚ")
                                   (newline)
                                   (menu)))
    (else(begin
           (newline)
           (newline)
           (display "Nombre del contacto ")(display x)(display ": ")
           (display (agenda-name (list-ref listaagenda x)))
           (newline)
           (display "Cédula del contacto ")(display x)(display ": ")
           (display (agenda-cc (list-ref listaagenda x)))
           (newline)
           (display "Dirección del contacto ")(display x)(display ": ")
           (display (agenda-address (list-ref listaagenda x)))
           (newline)
           (display "Telefono del contacto ")(display x)(display ": ")
           (display (agenda-number (list-ref listaagenda x)))
           (showdatas (+ x 1))))
    )
  )


;Función del menu principal desde el que se accede a los demas menus
(define (menu)
  (begin
    (displayln "AGENDA TELEFÓNICA")
    (newline)
    (displayln "Digite 1 para agregar nuevos datos de contacto")
    (displayln "Digite 2 para consultar datos")
    (displayln "Digite 3 para salir del programa")
    (displayln "Ingrese su opción: " )
    (set! menucontroller (read))
    (cond
      ((not(number? menucontroller))(begin
                                       (displayln "ERROR,SE REINICIARA EL MENÚ")
                                       (newline)
                                       (menu)))
      ((= menucontroller 1) (userdatas))
      ((= menucontroller 2) (menudatas))
      ((= menucontroller 3) (displayln "FIN DE LA AGENDA"))
      
      (else(begin
             (displayln "ERROR,SE REINICIARA EL MENÚ")
             (menu))))))

;Menú desde el que se consultan los datos
(define (menudatas)
  (begin
    (newline)
    (displayln "MENÚ DE CONSULTA DE DATOS")
    (newline)
    (displayln "Digite 1 para consultar todos los datos: ")
    (displayln "Digite 2 para consultar datos por nombre: ")
    (displayln "Digite 3 para volver al menú principal: ")
    (displayln "Ingrese su opción: ")
    (set! menudatascontroller (read))
    (cond
      ((= menudatascontroller 1)(showdatas 0))
      ((= menudatascontroller 2)(datasbyname))
      ((= menudatascontroller 3)(menu))
      (else (begin
              (displayln "ERROR DE DIGITACIÓN, SE LE DEVOLVERA AL MENÚ DE CONSULTA DE DATOS")
              (menu))))))

;Menú de busqueda de contactos por nombre
(define(datasbyname)
  (begin
    (newline)
    (displayln "DIGITACIÓN POR NOMBRE")
    (newline)
    (displayln "Digite el nombre del contacto guardado (entre comillas dobles y recuerde digitarlo correctamente): ")
    (set! namedatas (read))
    (cond
      ((string? namedatas) (datasfinder 0))
      ((not(string? namedatas)(begin
                                (newline)
                                (displayln "ERROR, SE REINICIARA EL BUSCADOR POR NOMBRE")
                                (datasbyname))))
      (else(begin
             (newline)
             (displayln "ERROR DE DIGITACIÓN, SE REINICIARA EL BUSCADOR POR NOMBRE")
             (datasbyname))))))
   
    

;Función auxiliar del menú de contactos por nombre
(define (datasfinder y)
    (cond
      ((empty? listaagenda)(begin
                             (newline)
                             (displayln "NO HAY CONTACTOS GUARDADOS")
                             (menudatas)))
      ((> y (length listaagenda)) (begin
                                    (newline)
                                    (displayln "El contacto que busca no esta en la agenda")
                                    (newline)
                                    (menudatas)))
      ((not(equal? namedatas (agenda-name (list-ref listaagenda y))))(datasfinder (+ y 1)))
                                                                     
      ((equal? namedatas (agenda-name (list-ref listaagenda y)))(begin
                                                                  (newline)
                                                                  (newline)
                                                                  (displayln "DATOS DEL CONTACTO QUE SE BUSCA: ")
                                                                  (newline)
                                                                  (newline)
                                                                  (display "Nombre del contacto ")(display y)(display ": ")
                                                                  (display (agenda-name (list-ref listaagenda y)))
                                                                  (newline)
                                                                  (display "Cédula del contacto ")(display y)(display ": ")
                                                                  (display (agenda-cc (list-ref listaagenda y)))
                                                                  (newline)
                                                                  (display "Dirección del contacto ")(display y)(display ": ")
                                                                  (display (agenda-address (list-ref listaagenda y)))
                                                                  (newline)
                                                                  (display "Telefono del contacto ")(display y)(display ": ")
                                                                  (display (agenda-number (list-ref listaagenda y)))
                                                                  (newline)
                                                                  (displayln "FIN DEL CONTACTO, SE LE DEVOLVERA AL MENÚ DE CONSULTA DE DATOS")
                                                                  (newline)
                                                                  (newline)
                                                                  (menudatas)))
      (else(begin
             (newline)
             (displayln "ERROR, SE LE DEVOLVERA AL MENÚ DE CONSULTA DE DATOS")
             (newline)
             (newline)
             (menudatas)))))
       
       
       
(menu)