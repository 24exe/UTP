#lang racket

;Contrato: Reversa: lista -> listsa invertida
;Propósito: Invertir el orden de elementos de una lista sin usar la función predeterminada "reverse"
;Ejemplo: (reversefun '(1 2 3) retornara '(3 2 1)
;Parámetros: num

;Variables Globales
(define listex '(1 2 3 4 5 6 7 8 9))
(define listreverse '())

;Función Principal que se encarga de invertir los elementos de una lista 
(define (reversefun list cont)
  (cond
    ((null? list) (displayln "error"))
    ((= cont (length listex)) (displayln listreverse))
    (else (begin
            (set! listreverse (cons (list-ref listex cont) listreverse))
            (reversefun list (+ cont 1))
            ))
    )
  )

;Prueba
(reversefun listex 0)