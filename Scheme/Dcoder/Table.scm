;guile 2.0.9
(use-modules (ice-9 format))
(let ((n (read)))
	(do ((i 1 (+ i 1)))
		((> i 10)) 
		(format #t "~d~%" (* n i))))