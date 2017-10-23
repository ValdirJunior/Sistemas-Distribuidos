<?php
// server
class SoapIMC
{

    private $peso;
    private $altura;
    private $idade;
    private $nome;

    public function getMessage($nome)
    {
        $this->nome = $nome;
        return 'Hello, '.$this->nome;
    }

    public function idade($idade)
    {
        $this->idade = $idade;
        return $this->idade;
    }

    public function getIMCMessage()
    {
        return "\nSeu IMC é de: ";
    }

    public function getIMC($peso, $altura)
    {
        return round($peso/($altura*$altura),2);
    }
}

$options= array('uri'=>'http://localhost/6_soap/');
$server=new SoapServer(NULL,$options);
$server->setClass('SoapIMC');

$server->handle();
