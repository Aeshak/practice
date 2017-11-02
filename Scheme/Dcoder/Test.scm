;guile 2.0.9
(define x "Hello, Dcoder!")
(do ((i 0 (+ i 1)))
	((= i (string-length x)))
	(display (string-append (string (string-ref x i)) "?")))