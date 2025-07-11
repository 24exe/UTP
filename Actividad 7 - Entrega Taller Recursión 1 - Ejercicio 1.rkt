#lang racket

;Contrato: mult: número número --> multiplicación de estos números
;Propósito: multiplicar 2 números solo con el operador de suma
;Ejemplo: (mult 20 4) retornara el número 80
;Parámetros: a b


;Función principal
(define (mult a b)
  (cond
    ((= b 0) 0)
    (else(+ a (mult a (- b 1))))
))

;Prueba:
(mult 20 4)

