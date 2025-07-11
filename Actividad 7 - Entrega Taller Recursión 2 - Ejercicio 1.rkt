#lang racket

;contrato: número => tablas
;propósito: imprimir las tablas desde el número x hasta la del 10
;ejemplo: (tablasfinal 9) =>
#|
9 * 1 = 9
9 * 2 = 18
9 * 3 = 27
9 * 4 = 36
9 * 5 = 45
9 * 6 = 54
9 * 7 = 63
9 * 8 = 72
9 * 9 = 81
9 * 10 = 90

10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
10 * 6 = 60
10 * 7 = 70
10 * 8 = 80
10 * 9 = 90
10 * 10 = 100

Final de las tablas
|#

;funcion auxiliar encargada de imprimir las tablas
(define (tabla a b)
  (cond
    ((<= a 0)(display "error"))
    ((> a 10) (displayln ""))
    (else (begin
            (display b)
            (display " * ")
            (display a)
            (display " = ")
            (displayln (* b a))
            (tabla (+ a 1) b)
            ))
    )
  )

;función auxiliar
(define (tablasfinal a)
  (cond
    ((<= a 0)(display "error"))
    ((> a 10)(display ""))
    (else (begin
            (tabla 1 a)
            (tablasfinal (+ a 1))
            ))
    )
  )

;función principal encargada de pedir el número al usuario
(define (fun)
  (displayln "Digite un número del 1 al 10 para mostrar tablas: ")
  (tablasfinal (read))
  (displayln "Final de las tablas")
  )

(fun)