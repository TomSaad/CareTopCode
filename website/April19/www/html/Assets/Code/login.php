<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="../Style/style_login.css">
</head>
<body style="background:#EAEFBD">
    <?php
        $path = "../Data/users.txt";
        $fh = fopen($path, "r");
        $usrId =  fread($fh, 8);
        fread($fh, 1);
        $usrPass = fread($fh, 12);
        $usrPass = trim($usrPass, ".");
        //echo $usrPass;
        //echo "\n";
        //echo $_POST["psw"];
        //echo "\n";
        //echo $usrId;
        //echo "\n";
        //echo $_POST["tankId"];
    ?>
    
    <h1 style="color:black;font-size:15vw;font-family:Tribeca Regular;" align="center">
        <?php
    	    if ($usrPass == $_POST["psw"] and $usrId == $_POST["tankId"]) {
    	        echo '<script>window.location.href = "../../caretop_main.html";</script>';
    	    } else {
    	        echo "LOGIN FAILED";
    	    }
    	?>
    </h1>
    
</body>
</html>