#lang racket

;Contrato: Unión: lista1 lista2 -> lista unida
;Propósito: unir dos listas dadas por el usuario sin el uso de la función predefinida "append" o "map"
;Ejemplo: (bond '(1 2 3) '(4 5 6)) retorna '(1 2 3 4 5 6)
;Parámetros: lista1 lista2

;Variables globales de las listas que luego seran llenadas
(define listfinal1 '())
(define listfinal2 '())

;Función Auxiliar que une las dos listas
(define (bond list1 list2 cont)
  (cond
    ((null? list) (displayln "error"))
    ((= cont (length list1)) (displayln list2))
    (else (begin
            (set! list2 (cons (list-ref (reverse list1) cont) list2))
            (bond list1 list2 (+ cont 1))
            ))
    )
  )

;Función Principal que pregunta al usuario las listas 
(define (fun)
  (displayln "digite una lista (entre parentesis): ")
  (set! listfinal1 (read))
  (displayln "digite otra lista (entre parentesis): ")
  (set! listfinal2 (read))
  (bond listfinal1 listfinal2 0)
  )

;Prueba
(fun)






