Program Ochered;
Uses Crt;
Const n=1000;
Var i,j: integer; x,P,Q: real;
    A,B,C,D,E,F,G: array [1..n] of real;
    H, L: array [1..11] of real;
begin
  randomize;
  P:=10;
  Q:= 5;
  A[1]:= random*P;
  B[1]:=random*Q;
  C[1]:= 0;
  D[1]:= 0;
  E[1]:= D[1] + B[1];
  F[1]:= E[1]-C[1];
  G[1]:= 0;
  for i:= 2 to n do
  begin
    A[i]:= random*P;
    B[i]:=random*Q;
    C[i]:= C[i-1]+A[i];
    if c[i]>E[i-1] then
      D[i]:= C[i]
    else
      D[i]:= E[i-1];
    E[i]:=D[i] + B[i];
    F[i]:= E[i]-C[i];
    G[i]:= F[i]-B[i];
  end;
  x:= G[i]
  for i:=2 to n do
    if G[i]>x then
      x:= G[i];
    writeln('Максимальное значение G = ', x);
    x:= G[1];
    for i:= 2 to n do
      x:= x + G[i];
    x:= x/n;
    writeln('Среднее значение G = ', x);
    x:= P;
    for i:=1 to 11 do
      L[i]:= (i-1)*x/10;
    for i:=1 to 11 do
      H[i]:= 0;
    for i:= 1 to 10 do
      for j:=1 to n do
        if ((G[j]>=L[i]) and (G[j]<L[i+1])) then
          H[i]:= H[i] + 1;
    for j:=1 to n do
      if (G[j]>=P) then
        H[11]:= H[11] + 1;
    for i:= 1 to 11 do
      H[i]:= H[i]/n;
    for i:=1 to 11 do
      writeln('G[', i, ']=', H[i]);
    repeat until keypressed
end.
