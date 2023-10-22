program SampleProgram;

{$DEFINE DEBUG}
{$IFDEF DEBUG}
  // Це коментар
  writeln('Debug mode is active.');
{$ENDIF}
var
  num1, num2: integer;
  str: string;

begin
  num1 := 10;
  num2 := 20;
  str := 'Hello, World!';

  if num1 > num2 then
    writeln('num1 is greater than num2')
  else
    writeln('num2 is greater than or equal to num1');
end.