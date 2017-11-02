;guile 2.0.9
(use-modules (ice-9 format))
(use-modules (ice-9 rdelim))
(let ((n (read-line)))
	(define lst (string->list  n))
	(set! lst (map (lambda (x) 
					(if (eqv? x #\1) #\0
					#\1))  lst))
	(display (list->string lst)))
    