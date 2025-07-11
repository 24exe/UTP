#lang racket


;contrato costo: número número => número
;proposito: determinar el costo de la carrera seleccionada de acuerdo al estrato de la persona
;ejemplo: (costo 1 2) => 960000

;variable que contendra el estrato
(define estrato 0)
;variable que contendra un valor númerico que equilvadrá a la carrera
(define carrera 1)


;función auxiliar para calcular el valor de la carrera según el porcentaje a restar
(define (CalcPorcentaje porcentaje valor)
  (define descuento (/(* valor porcentaje)100))
  (- valor descuento)
  )

;función auxiliar para calcular el porcentaje según el estrato 
(define (CostoCarrera estrato valor)
  (cond
    ((= estrato 1) (CalcPorcentaje 20 valor))
    ((= estrato 2) (CalcPorcentaje 10 valor))
    (else valor)
    )
  )

;función auxiliar para mostrar el nombre de la carrera y el costo de forma ordenada
(define (Datos carrera costo)
  (display "La ")
  (display carrera)
  (display " tiene un costo de: ")
  (display costo)
  )
;función auxiliar para de acuerdo a la carrera elegida y el estrato retornar el valor, llama a la función para mostrar los datos y le pasa el retorno de la función para calcular el costo para ser mostrados
(define (costo carrera estrato)
  (cond
    ((= carrera 1) (Datos "Tecnología Electrónica" (CostoCarrera estrato 1000000)))
    ((= carrera 2) (Datos "Licenciatura Matemáticas" (CostoCarrera estrato 1200000)))
    ((= carrera 3) (Datos "Tecnología de Sistemas" (CostoCarrera estrato 1300000)))
    (else (display "carrera no disponible"))
    )
  )

;función principal donde se pedirán los datos de estrato y carrera al usuario y se llamara a la función calcCost para calcular el precio
(define (main)
  (displayln "Digite el estrato al q pertenece: ")
  (displayln "Digite (1) para estrato 1")
  (displayln "Digite (2) para estrato 2")
  (displayln "Digite (3) para otro estrato")
  (set! estrato (read))
  (displayln "Digite 1 para Tecnología Electrónica")
  (displayln "Digite 2 para Licenciatura en Matemáticas")
  (displayln "Digite 3 para Tecnología en Sistemas")
  (displayln "digite la carrera: ")
  (set! carrera (read))
  (costo carrera estrato)
  )
;prueba
(main)