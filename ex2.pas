program Ex1;
type matrix = array [1..5, 1..5] of integer;
var a: matrix;
    i, j, s: integer;
begin
  randomize;
  for i:=1 to 5 do
  begin
    for j:= 1 to 5 do
    begin
      a[i, j]:= random(100) - 50;
    end;
  end;
  for i:=1 to 5 do
  begin
    s:= 0;
    for j:= 1 to 5 do
    begin
      if a[i, j] < 0 then
        s:= s + 1;
    end;
    if (s = 2) then
      begin
      writeln('Да');
      exit;
      end;
  end;
end.
  
