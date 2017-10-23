<?php

require "vendor/autoload.php";

use GuzzleHttp\Client;

$client = new Client();

$response = $client->get('http://viacep.com.br/ws/17526693/json/');
echo $response->getBody();


 ?>
