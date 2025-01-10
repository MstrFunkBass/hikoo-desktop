powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Background Refreshing; Haiku Incoming!', 'Notification')"

cd /d %~dp0

cd ../..

call .venv\Scripts\activate

python hikoo-desktop\main.py

deactivate

powershell -Command "Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('Background Refresh Successful!', 'Notification')"