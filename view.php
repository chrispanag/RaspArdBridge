<?

$host    = "127.0.0.1";
$port    = 4096;

// create socket
$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Could not create socket\n");
// connect to server
$result = socket_connect($socket, $host, $port) or die("Could not connect to server\n");
// get server response
$result = socket_read ($socket, 1024) or die("Could not read server response\n");
// close socket
socket_close($socket);
?>

<html>
<head>
 <title>What the Arduino Says?</title>
</head>
<body>
 <p>The arduino says: <?php echo $result;?> </p>
</body>
</html>
