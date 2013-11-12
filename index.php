<?php

if(isset($_GET['soff'])) {

rename('shutter.wav','shutteroff.wav');

}

if(isset($_GET['son'])) {

rename('shutteroff.wav','shutter.wav');

}

exec('capture.py');

date_default_timezone_set('America/Los_Angeles');


$fp = fopen("log.log", "a");
 
fwrite($fp, date("F j, Y, g:i a")."\r\n");
?>

<img src="image.jpg">'