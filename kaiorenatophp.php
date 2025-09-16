<!DOCTYPE html>
<html lang="pt-br">
<head>
    <
    <meta charset="UTF-8">
    <title>Formulário de Kaio Mariano</title>
</head>
<body>

    <form method="POST">
        <input type="text" placeholder="Digite seu nome aqui" name="nome">
        <input type="text" placeholder="Digite sua idade aqui" maxlength="2" name="idade">
        <input type="submit" value="Enviar">
    </form>

    <?php
        $nome = htmlspecialchars($_POST["nome"]);
        $idade = htmlspecialchars($_POST["idade"]);

        echo "<p>Olá, $nome. Você tem $idade anos.</p>";
    ?>

</body>



</html>
