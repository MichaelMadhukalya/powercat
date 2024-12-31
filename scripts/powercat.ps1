# netcat like utility for windows using powershell
# usage: .\powercat -Address "127.0.0.1" -Port 80
# or .\powercat -Dns "localhost" -Port 80
param ( 
    [string]$Address = "127.0.0.1", 
    [string]$Dns = "localhost",
    [int]$Port = 80
)

Add-Type -AssemblyName "System.Net"
$socket = New-Object System.Net.Sockets.Socket(
    [System.Net.Sockets.AddressFamily]::InterNetwork, 
    [System.Net.Sockets.SocketType]::Stream, 
    [System.Net.Sockets.ProtocolType]::Tcp
)
if ([string]::IsNullOrEmpty($Address) -and [string]::IsNullOrEmpty($Dns)) {
    Write-Output "Either host Address or Dns is required"
} 
elseif (-not [string]::IsNullOrEmpty($Dns)) {
    $Address = [System.Net.Dns]::GetHostByName($Dns).AddressList[0]
}
Write-Output "Connecting to $Address at port $Port ..."
$socket.Connect($Address, $Port)
while ($true) {
    $input = Read-Host
    $byteArray = [System.Text.Encoding]::ASCII.GetBytes($input)
    [void]$socket.Send($byteArray) 
}
$socket.Close()