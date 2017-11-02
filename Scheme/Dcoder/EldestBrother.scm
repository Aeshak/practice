;guile 2.0.9
(use-modules (ice-9 format))
#|
(do ((x 0 (+ x 1)))
	((= x 10))
	(let ((n (read))) 
		(display n)))
	;(format #t "~d~%" n))
|#
(define MAX 0)
(while #t
	(let ((n (read))) 
		(if (eof-object? n) (break)
			(if (> n MAX) (set! MAX n)))))
(format #t "~d~%" MAX)