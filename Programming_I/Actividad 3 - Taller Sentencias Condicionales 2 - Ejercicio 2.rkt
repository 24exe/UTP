#lang racket

;contrato: checkout: número => número
;próposito: determinar los intereses a pagar de un banco según el monto de una compra de un usuario
;ejemplo: 

(define (intereses valor)
  (cond
       ((> valor 2500000) (+(+(+(/(* 500000 0.25)100)(/(* 1000000 0.50)100) ) (/(* 1000000 0.75)100) ) (/(* (- valor 2500000 ) 0.90)100) ))
       ((> valor 1500000) (+(+(+(/(* 500000 0.25)100)(/(* 1000000 0.50 )100) ) (/(* (- valor 1500000 ) 0.75)100) ) ))
       ((> valor 1000000) (+(+(/(* 500000 0.25)100)(/(* (- valor 500000) 0.50 )100))))
       ((> valor 0) (/(* valor 0.25)100))
  ))

(intereses 2000000)
(intereses 2600000)