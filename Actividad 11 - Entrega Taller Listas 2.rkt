#lang racket
;Contrato: Agenda
;Propósito: Agenda Telefonica en la que se pueden agendar contactos con sus respectivos parametros,
;se pueden consultar los contactos, agregar nuevos y demas.


;Variables Globales que seran reemplazadas posteriormente
(define listaagenda '())

(define-struct agenda (name cc address number))

(define menucontroller 0)
(define datascontroller 0)
(define name "")
(define cc "")
(define address "")
(define number "")

;Función auxiliar que pide los datos de un nuevo contacto y los agrega a una lista
(define (userdatas)
  (begin
    (displayln "Digite su nombre (entre comillas dobles): ")
    (newline)
    (set! name (read))
    (display "Digite su cédula (entre comillas dobles): ")
    (newline)
    (set! cc (read))
    (displayln "Digite su dirección (entre comillas dobles): ")
    (newline)
    (set! address (read))
    (displayln "Digite su número telefonico (entre comillas dobles): ")
    (newline)
    (set! number (read))
    (set! listaagenda (cons (make-agenda name cc address number)listaagenda))
    (newline)
    (displayln "Si desea agregar otro contacto marque 1, si desea volver al menú, marque 2")
    (set! datascontroller (read))
    (cond
      ((= datascontroller 1) (userdatas))
      ((= datascontroller 2) (menu))
      (else(begin
             (displayln "ERROR,SE LE DEVOLVERA AL MENÚ")
             (menu)
             )))))

;Función auxiliar encargada de mostrar los contactos guardados
(define (showdatas x)
  (cond
    (( = x (length listaagenda)) (begin
                                   (newline)
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


;Función Principal en la que el usuario interactua con el programa:
(define (menu)
  (begin
    (displayln "AGENDA")
    (displayln "Digite 1 para agregar un contacto")
    (displayln "Digite 2 para ver la lista de contactos")
    (displayln "Digite 3 para salir del menú")
    (set! menucontroller (read))
    (cond
      ((= menucontroller 1) (userdatas))
      ((= menucontroller 2) (begin
                              (displayln "LISTADO DE CONTACTOS")
                              (showdatas 0)))
      ((= menucontroller 3) (displayln "FIN DE LA AGENDA"))
      (else(begin
             (displayln "ERROR,VUELVA AL MENÚ")
             (menu))))))

;Prueba
(menu)