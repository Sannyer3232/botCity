$exclude = @("venv", "bot_Fakturama-Sannyer.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "bot_Fakturama-Sannyer.zip" -Force