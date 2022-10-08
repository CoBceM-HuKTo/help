program ss;
var n: integer;
    no: string;
    strno: string;
    strnt: string;
    i: integer;
    strntt: string;
    
begin
  readln(n);
  str(n,no);
  if (length(no) = 4) then
      begin
        strno:= no[1:3];
        strnt:= no[3:5];
        
        for i:=length(strnt) downto 1 do
          begin
            strntt:=strntt+strnt[i];
          end;
        if (strno = strntt) then
          writeln(n, ' - это полиндром.')
        else 
          writeln(n, ' - это не полиндром.')
      end
  else
      writeln('В числе ', n, ', не 4 знака.')
end.