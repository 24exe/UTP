#lang racket
;contrato: número => booleano
;propósito: determinar si un número es primo, el algoritmo realiza divisiones desde 2 hasta el número dado menos 1,
;si alguna de estas divisiones da como residuo cero significa que el número no es primo ya que es divisible por
;otro número que no es uno y si mismo
;ejemplo: (Primo 3 2) => #t

;variable que contendra un valor booleano asociado a si el número es primo no
(define x #t)

;función auxiliar que hace todo el proceso

(define (Primo a cont)
  (cond
    ((< a 1)(display "ERROR"))
    ((> cont (- a 1))(display ""))
    (else (begin
            (if (= (remainder a cont) 0) (set! x #f) "")
            (Primo a (+ cont 1))
            ))
    )
  )
;función principal para pedirle al usuario un número, llamar a la función Primo y según el resultado mostrar por pantalla si es primo o no
(define (fun)
  (displayln "Digite un número para saber si es primo") 
  (define num (read))
  (Primo num 2)
  (if (equal? x #t) (displayln "Es primo") (displayln "no Es primo"))
  )



;prueba
(fun)