#lang racket

;Contrato: vern1: número número -->
;Propósito: retornar todos los números entre un número x y un número y, con sus respectivos cuadrados, cubos, raices cuadradas y raices cubicas
;Ejemplo: (vern1 16 20) retornara los siguientes números:
#|
20, 400, 8000, 4.47213595499958, 2.7144176165949063
19, 361, 6859, 4.358898943540674, 2.668401648721945
18, 324, 5832, 4.242640687119285, 2.6207413942088964
17, 289, 4913, 4.123105625617661, 2.571281590658235
16, 256, 4096, 4, 2.5198420997897464
|#
;Parámetros: n1 n2

;Función Principal
(define (vern1 n1 n2)
  (if (<= n1 n2)
      (begin
        (vern1 (+ n1 1) n2)
        (display  n1)
        (display ", ")
        (display (expt n1 2))
        (display ", ")
        (display (expt n1 3))
        (display ", ")
        (display (sqrt n1))
        (display ", ")
        (displayln (expt n1(/ 1 3))))
      (displayln "")
          )
      )
;Prueba
(vern1 16 20)

(newline)
(newline)

;Función con la que el usuario va a interactuar
(define (fin)
  (display "digite 2 números, tenga en cuenta que el primer número tiene que ser menor al segundo número: ")
  (vern1 (read)(read))
  )
(fin)