<#
 	Nested for-loops work by finishing everything inside itself before continuing.
 	The inner loop must finish all its iterations before the outer loop can continue
 	its next iteration.

 	E.g. Port scanner runs through each IP, then each IP gets each of the ports

 	IP gets each of the ports, then on to the next IP


 	Outer loop                            Inner loop
 	----------							  ----------
 	10.10.0.32: 8075, 8076, 8077, 8078, 8079, 8080, 8081, 8082, 8803, 8084, 8085

 	10.10.0.33: 8075, 8076, 8077, 8078, 8079, 8080, 8081, 8082, 8803, 8084, 808

#>


# Scan all IPs in CIDR block 10.10.0.32/29 from ports 8075-8085


(32..39) | % {$ip='10.10.0.'+$_;(75..85) | % {$port='80'+$_;$conn = New-Object -TypeName System.Net.Sockets.TcpClient;$set = $conn.BeginConnect($ip,$port,$null,$null);$response = $set.AsyncWaitHandle.WaitOne(500,$false); if ($response) {$conn.Close();echo $ip":"$port" is open!"}}} 2>$null