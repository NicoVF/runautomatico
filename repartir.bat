@echo off
cd autorepartir

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%"

echo[				    	>> log_%YYYY%_%MM%.log
echo[			            >> log_%YYYY%_%MM%.log

python autorepartidor.py    >> log_%YYYY%_%MM%.log
timeout 10
exit