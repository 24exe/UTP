#lang racket
;Contrato: Calculadora de dias que han transcurrido desde el 1 de enero del 2000
;Propósito: Calculadora de dias que han transcurrido desde el 1 de enero del 2000

;Variables Globales que seran reescritas con el valor que ingrese el usuario
(define day 0)
(define mounth 0)
(define year 0)

;Función principal que pregunta al usuario los datos y devuelve la cantidad de dias que han transcurrido desde el 1 de enero del 2000 hasta la fecha ingresada
(define (datas)
  (displayln "Ingrese el dia: ")
  (set! day (read))
  (displayln "Ingrese el mes: ")
  (set! mounth (read))
  (displayln "Ingrese el año: ")
  (set! year (read))
 (cond
    ((or (< day 1) (< mounth 1)) (displayln "ERROR, INGRESE UNA FECHA VALIDA, SE REINICIARA EL PROGRAMA") (datas))
    ((> day 31)(displayln "ERROR, INGRESE UN DIA INFERIOR A 31, SE REINICIARA EL PROGRAMA")(datas))
    ((> mounth 12) (displayln "ERROR, INGRESE UN AÑO INFERIOR A 12, SE REINICIARA EL PROGRAMA") (datas))
    ((< year 2000) (displayln "ERROR, INGRESE UN AÑO SUPERIOR A 2000") (datas))
    (else (begin
            (newline)
            (displayln "Desde el 1 de Enero del 2000 ha transcurrido exactamente esta cantidad de dias: ")
            (date 1 1 2000 0 4)))
    )
  )

;Función auxiliar que cuenta los dias que tiene un mes 
(define (mounthcount m y)
  (cond
    [(or (= m 1) (= m 3) (= m 5) (= m 7) (= m 8) (= m 10) (= m 12)) 31]
    [(or (= m 4) (= m 6) (= m 9) (= m 11)) 30]
    [(= m 2) (if (= (remainder y 4) 0) 29 28)]
    )
  )

;Función auxiliar que cuenta los dias, los almacena y luego retorna a la funcion principal
(define (date d m a cont bis)
  (if (= d day)
      (if (= m mounth)
          (if (= a year)
              cont
              (date d (+ m 1) a (+ cont (mounthcount m a)) bis)
              )
          (begin
            (if (= m 13)
                (date d 1 (+ a 1) cont (+ bis 1))
                (date d (+ m 1) a (+ cont (mounthcount m a)) bis))))
      (begin
        (date day m a (+ cont (- day 1)) bis))))

(datas)

