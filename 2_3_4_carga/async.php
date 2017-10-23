<?php

require "vendor/autoload.php";

use GuzzleHttp\Client;

$client = new Client();

$promise = $client->getAsync('http://viacep.com.br/ws/17526693/json/');
$promise->then(
    function($response) {
        echo $response->getBody();
    }
);
$promise->wait();

 ?>
