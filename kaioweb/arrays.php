<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $notaTxt = $_POST['notas'] ?? '';
    $notaArr = explode(',',$notaTxt);
    $notaNum = [];
    foreach ($notaArr as $n) {
        $notaNum [] = (float)trim($n);
    }

    function calcmedaia($nota) {
        if (count($nota) === 0)
            return 0;
        $soma = array_sum($nota);
        $media = $soma / count($nota);
        return $media;


    }
}



?>