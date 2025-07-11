#lang racket

;Contrato: num: número --> x cantidad de números
;Propósito: mostrar en pantalla los números desde ese hasta el 10
;Ejemplo: (num 3) retornara los números desde el 3 al diez así:
#|
3
4
5
6
7
8
9
10
|#
;Parámetros: x


;Función principal
(define (num x)
  (cond
    ((= x 11) display "fin")
    ((< x 0) displayln "ERROR")
    (else (begin
           (display x)
           (newline)
           (num (+ x 1))
           (newline)
           )
          )
    )
  )

;Prueba

(num 3)

