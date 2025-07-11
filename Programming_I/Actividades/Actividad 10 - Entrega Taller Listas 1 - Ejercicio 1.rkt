#lang racket

;Contrato: Incrementar: lista -> lista con cada elemento incrementado en 100 
;Propósito: función que incremente en 100 los números de una lista.
;Ejemplo: ((listfun '(1 2 3 4 5)) retorna '(101 102 103 104 105)
;Parámetros: list1

;variable global que contiene la lista que se va a incrementar
(define list1 '( 1 2 3 4 5))

;función auxiliar que incrementa cada elemento de la lista en 100
(define (increase n)
  (+ n 100)
  )

;función principal para incrementar en 1oo los números de la lista
(define (listfun list)
  (map increase list)
  )

;prueba
(listfun list1)
