<!DOCTYPE HTML>
<html>
<head>
</head>
<body>

<?php
    //Start by making the JS file
    $path = "../Data/config.js";
    $fh = fopen($path, "w");
    $path = "../Data/config.json";
    $f = fopen($path, "w");

    fwrite($fh, "var config = {\n");
    fwrite($f, "{\n");

    $text = '"created": "' . date("D M j H:i:s Y") . "\",\n";
    fwrite($fh, $text);
    fwrite($f, $text);

    $t = $_POST["start_date"];
    $date = explode("-", $t);
    $t = $_POST["start_time"];
    $text = '"start": [' . $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
    $text_json = '"start": "' . $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    fwrite($fh, $text);
    fwrite($f, $text_json);

    if (date("Y") >= $date[0] && date("m") >= $date[1] && date("j") >= $date[2] && date("H") >= $t) {
        $r = "true";
    } else {
        $r = "false";
    }
    $text = '"running": ' . $r . ",\n";
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $t = $_POST["temp"];
    $text = '"dTemp": ' . $t . ",\n";
    fwrite($fh, $text);
    fwrite($f, $text);

    $t = $_POST["hum"];
    $text = '"dHum": ' . $t . ",\n";
    fwrite($fh, $text);
    fwrite($f, $text);

    //I KNOW, A FOR LOOP WOULD HAVE MADE THIS SO EASY
    //I FELT LIKE HARD CODING, OK, THATS OK SOMETIMES
    //I WAS SUPER FRUSTRATED WITH PHP RANDOMLY CRAPPING
    //OUT SO THIS WAS MORE ROBUST WHEN IT DECIDED TO HAVE A 
    //MOMENT :(:(:(

    $text = '"feeding1": [';
    $text_json = '"feeding1": "';
    if( $_POST["f1_date"] != "" && $_POST["f1_time"] != "" ) {
        $t = $_POST["f1_date"];
        $date = explode("-", $t);
        $t = $_POST["f1_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding2": [';
    $text_json = '"feeding2": "';
    if( $_POST["f2_date"] != "" && $_POST["f2_time"] != "" ) {
        $t = $_POST["f2_date"];
        $date = explode("-", $t);
        $t = $_POST["f2_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding3": [';
    $text_json = '"feeding3": "';
    if( $_POST["f3_date"] != "" && $_POST["f3_time"] != "" ) {
        $t = $_POST["f3_date"];
        $date = explode("-", $t);
        $t = $_POST["f3_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding4": [';
    $text_json = '"feeding4": "';
    if( $_POST["f4_date"] != "" && $_POST["f4_time"] != "" ) {
        $t = $_POST["f4_date"];
        $date = explode("-", $t);
        $t = $_POST["f4_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding5": [';
    $text_json = '"feeding5": "';
    if( $_POST["f5_date"] != "" && $_POST["f5_time"] != "" ) {
        $t = $_POST["f5_date"];
        $date = explode("-", $t);
        $t = $_POST["f5_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding6": [';
    $text_json = '"feeding6": "';
    if( $_POST["f6_date"] != "" && $_POST["f6_time"] != "" ) {
        $t = $_POST["f6_date"];
        $date = explode("-", $t);
        $t = $_POST["f6_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding7": [';
    $text_json = '"feeding7": "';
    if( $_POST["f7_date"] != "" && $_POST["f7_time"] != "" ) {
        $t = $_POST["f7_date"];
        $date = explode("-", $t);
        $t = $_POST["f7_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding8": [';
    $text_json = '"feeding8": "';
    if( $_POST["f8_date"] != "" && $_POST["f8_time"] != "" ) {
        $t = $_POST["f8_date"];
        $date = explode("-", $t);
        $t = $_POST["f8_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding9": [';
    $text_json = '"feeding9": "';
    if( $_POST["f9_date"] != "" && $_POST["f9_time"] != "" ) {
        $t = $_POST["f9_date"];
        $date = explode("-", $t);
        $t = $_POST["f9_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "],\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1],\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    $text = '"feeding10": [';
    $text_json = '"feeding10": "';
    if( $_POST["f0_date"] != "" && $_POST["f0_time"] != "" ) {
        $t = $_POST["f0_date"];
        $date = explode("-", $t);
        $t = $_POST["f0_time"];
        $text .= $date[0] . ", " . $date[1] . ", " . $date[2] . ", " . $t . "]\n";
        $text_json .= $date[0] . "&" . $date[1] . "&" . $date[2] . "&" . $t . "\",\n";
    } else {
        $text .= "-1]\n";
        $text_json .= "\"-1\",\n";
    }
    fwrite($fh, $text);
    fwrite($f, $text_json);

    fwrite($fh, "}");
    fwrite($f, "}");

    fclose($fh);
    fclose($f);

    //THEN MAKE THE JSON FILE
?>

<p>Settings Updating, please allow up to 1min for your careTop to update</p>
<button>
    <a href="../../caretop_main.html">Return to CareTop</a>
</button>

</body>
</html>
