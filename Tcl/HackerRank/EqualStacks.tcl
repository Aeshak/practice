#tclsh 8.6

set input [split [read stdin] \n]
set n1 [lindex $input 1]
set n2 [lindex $input 2]
set n3 [lindex $input 3]
proc sum {n} {
	set s 0
	foreach i $n {
		incr s $i
	}
	return $s
}
set h1 [sum $n1]
set h2 [sum $n2]
set h3 [sum $n3]
set i 0
set j 0
set k 0
set flag 1
while { $h1 != $h2 || $h2 != $h3 || $h1 != $h3} {
	if { $h1 == 0 || $h2 == 0 || $h3 == 0} {
		puts 0
		set flag 0
		break
	}
	if {$h1 > $h2 || $h1 > $h3} {
		incr h1 [expr -1*[lindex $n1 $i]]
		incr i
	} elseif {$h2 > $h1 || $h2 > $h3} {
		incr h2 [expr -1*[lindex $n2 $j]]
		incr j
	} elseif {$h3 > $h1 || $h3 > $h2} {
		incr h3 [expr -1*[lindex $n3 $k]]
		incr k
	} else {
		break
	}
}
if {$flag} {
	puts $h1
}
    