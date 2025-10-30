#lang plait

;-------------------------------------------------------------------------2
; wyrazenie = "`"dowtyp | formyspecialne
; dowtyp ::= boolean | liczbafin |znak | napis | symbol
; boolean = "#t" | "#f"
; liczbafin = liczba | liczba + 0*.liczba gdzie (0* oznacza ciag zer)
; napis = znak | napis "+s" znak (sklejanie)
; znak = dowolny znka ASCII 
; symbol = "'"wyrazenie
; formyspecialne = ' (wyrazenie * wyrazenie ) | `(wyrazenie * wyrazenie ) |
;            '(wyrazenie . wyrazenie ) | ' wyrazenie | `wyrazenie | , wyrazenie
; liczba = "0" | "1" | "2" ...
;--------------------------------------------------------------------------1


; wyrazenie = podwyra_1 | wyrazenie + podwyra_1 | wyrazenie - podwyra_1
; podwyra_1 = podwyra_2 | podwyra_1 * podwyra_2 | podwyra_1 / podwyra_2
; podwyra_2 = podwyra_3 | podwyra_2! | -podwyra_2
; podwyra_3 = podwyra_4 | podwyra_3 ^ podwyra_4
; podwyra_4 = liczbafin | -liczbafin | podwyra_4!
; liczbafin = liczba | liczba + 0.liczba
; liczba = "0" | "1" | "2" ...


