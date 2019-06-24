<?php
define("MOTERTEST", "/usr/bin/sudo /home/pi/motertest");
define("ADDRESS", "127.0.0.1");
define("USER", "pi");
define("PASSWORD", "PASSWORD");

/* SSH2 module processes */
$sconnection = ssh2_connect(ADDRESS, 22);
ssh2_auth_password($sconnection, USER, PASSWORD);
/* execution command */
$command = MOTERTEST;
$stdio_stream = ssh2_exec($sconnection, $command);


?>

