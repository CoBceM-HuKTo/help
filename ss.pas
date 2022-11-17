program Ex1;
type matrix = array [1..5, 1..5] of integer;
var a: matrix;
    i, j, s: integer;
    matrix2:array [1..5] of integer;
begin
  for i:=1 to 5 do
  begin
    for j:= 1 to 5 do
    begin
      readln(a[i, j]);
      
    end;
  end;
  for i:=1 to 5 do
  begin
    s:= 0;
    for j:= 1 to 5 do
    begin
      if (j mod 2 = 0) then
      begin
        if (a[i, j] > -1) then
          s:= s + a[i, j];
      end;
    end;
    matrix2[i]:= s;
  end;
  writeln(matrix2);
end.
  
