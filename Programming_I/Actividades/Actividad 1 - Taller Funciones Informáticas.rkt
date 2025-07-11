#lang racket
;Contrato: Conversor: número -> número
;Propósito: Convertir unidades, entre sistema metrico y sistema inglés
;Ejemplo: el ejemplo se dara en todos y cada uno de los programas de manera individual
;Parámetros: se daran en todos los programas correspondientes

;Funciones para hacer las respectivas conversiones mas adelante
(define pul-cm 2.54)
(define pie-pul 12)
(define yar-pie 3)
(define vara-yar 5.5)
(define furlong-vara 40)
(define milla-furlong 8)

#|
Contrato: Conversor: num en pulgadas -> num en centimetros
Propósito: Convertir unidades en pulgadas a centimetros
Ejemplo: (pulcmp 20) debe dar: 50.8
Parametros: num
|#

(define (pulcmp x)
  (* x pul-cm)
  )
;Prueba:
(pulcmp 20)

#|
Contrato: Conversor: num en pies -> num en pulgadas
Propósito: Convertir unidades en pies a pulgadas
Ejemplo: (piepulp 20) debe dar: 240
Parametros: num
|#

(define (piepulp x)
  (* x pie-pul)
  )

;Prueba:
(piepulp 20)

#|
Contrato: Conversor: num en yardas -> num en pies
Propósito: Convertir unidades en yardas a pies
Ejemplo: (yarpiep 20) debe dar: 60
Parametros: num
|#

(define (yarpiep x)
  (* x yar-pie)
  )
;Prueba:
(yarpiep 20)

#|
Contrato: Conversor: num en varas -> num en yardas
Propósito: Convertir unidades en varas a yardas
Ejemplo: (varayarp 20) debe dar: 110
Parametros: num
|#

(define (varayarp x)
  (* x vara-yar)
  )

;Prueba:
(varayarp 20)

#|
Contrato: Conversor: num en furlongs -> num en varas
Propósito: Convertir unidades en furlongs a varas
Ejemplo: (furvarp 20) debe dar: 800
Parametros: num
|#

(define (furvarp x)
  (* x furlong-vara)
  )

;Prueba:
(furvarp 20)

#|
Contrato: Conversor: num en millas -> num en furlongs
Propósito: Convertir unidades en millas a furlongs
Ejemplo: (milfurp 20) debe dar: 160
Parametros: num
|#

(define (milfurp x)
  (* x milla-furlong)
  )

;Prueba
(milfurp 20)

#|
Contrato: Conversor: num en pies -> num en centimetros
Propósito: Convertir unidades en pies a centimetros
Ejemplo: (piescmp 20) debe dar: 609.6
Parametros: num
|#

(define (piescmp x)
  (pulcmp(piepulp x)
     )
  )
;Prueba
(piescmp 20)

#|
Contrato: Conversor: num en yardas -> num en centimetros
Propósito: Convertir unidades en yardas a centimetros
Ejemplo: (yarcmp 20) debe dar: 1828.8
Parametros: num
|#

(define (yarcmp x)
  (piescmp(yarpiep x)
          )
  )
;Prueba
(yarcmp 20)

#|
Contrato: Conversor: num en varas -> num en pulgadas
Propósito: Convertir unidades en varas a pulgadas
Ejemplo: (varpulp 20) debe dar: 3960
Parametros: num
|#

(define (varpulp x)
  (piepulp(yarpiep (varayarp x)))
  )
;Prueba
(varpulp 20)

#|
Contrato: Conversor: num en millas -> num en pies
Propósito: Convertir unidades en millas a pies
Ejemplo: (millaspiesp 20) debe dar: 105600
Parametros: num
|#

(define (millaspiesp x)
  (yarpiep(varayarp(furvarp(milfurp x))))
  )
;Prueba
(millaspiesp 20)
