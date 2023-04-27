Program Sluch_chisla;
Const Ntab=10000;
Var i, j, k: integer; a:real; z: array [1..Ntab] of real; b:array [1..20] of real; c:array [1..21] of real;
Procedure Puasson(n: integer; Ax, Ay:real; Var Tab: array [1..Ntab] of real);
Var x,y: real; i : integer;
begin
    i:=1;
    while i <= Ntab do
    begin
      x:= random*Ax;
      y:= random*Ay;
      if y<(power(x,n)*exp(-x)/n) then
      begin
        Tab[i]:= x;
        i:= i + 1
      end
    end
end;

begin
  randomize;
  Puasson(2,10,0.3,z);
  k:= 20;
  for i:= 1 to k + 1 do
    c[i]:= (i-1)*10/k;
  for i:=1 to k do
  begin
    b[i]:=0;
    for j:=1 to Ntab do
      if ((z[j]>c[i]) and (z[j] <= c[i + 1])) then
        b[i]:=b[i] + 1
  end;
  for i:=1 to k do
    b[i]:= b[i]/Ntab*2;
  for i:=1 to k do
    Writeln('I=', i:4, 'c=', c[I]:6:2, '  b=', b[i]:8:4)
end.
