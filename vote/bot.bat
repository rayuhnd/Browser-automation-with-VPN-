
:loop

taskkill /F /IM VPN.exe
taskkill /F /IM geckodriver.exe

echo STARTING...
start "" "C:\Users\ryans\OneDrive\Desktop\vote\VPN.exe"

timeout /t 7 /nobreak >nul

echo [!] Starting the Voting process...
python "C:\Users\ryans\OneDrive\Desktop\vote\vote.py"

timeout /t 7 /nobreak >nul

echo [+] Voting done.
taskkill /F /IM geckodriver.exe

timeout /t 7 /nobreak >nul

echo Killing the VPN
taskkill /F /IM VPN.exe

echo Closing browser   
python "C:\Users\ryans\OneDrive\Desktop\vote\vote2.py"

goto loop