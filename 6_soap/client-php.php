<?php

$options = array(
    'uri' => 'http://localhost/6_soap/',
    'location' => 'http://localhost/6_soap/server.php'
);

$client = new SoapClient(null, $options);

echo $client->getMessage('Valdir');
$client->idade(21);
echo $client->getIMCMessage();
echo $client->getIMC(75, 1.81);

 ?>
