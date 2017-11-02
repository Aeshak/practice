//fpc 3.0.0

program of_example;
var
		a, b, c, d: integer;
begin
		while not eof do begin
			read(a);
			read(b);
			c := Abs(a-b);
			d := Abs(a+b);
			if (c = 6) or (d = 6) then
				writeln('Love')
			else
				writeln('Hate');
		end
end.