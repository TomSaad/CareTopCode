//var myVar = setInterval(function(){ Start() }, 5000);
var temp_avg, hum_avg;

function Start() {
    readTemp();
    readHum();
    readLight();
    readDate();
    test();
}

function test() {
    console.log("Test");
}

function readTemp() {
    temp_avg = data["temp0"] + data["temp1"] + data["temp2"] + data["temp3"] + data["temp4"];
    temp_avg /= 5;
    console.log("Updating Temp");
    document.getElementById("temp_avg").innerHTML = temp_avg;
    document.getElementById("temp_0").innerHTML = data["temp0"];
    document.getElementById("temp_1").innerHTML = data["temp1"];
    document.getElementById("temp_2").innerHTML = data["temp2"];
    document.getElementById("temp_3").innerHTML = data["temp3"];
    document.getElementById("temp_4").innerHTML = data["temp4"];
}

function readHum() {
    hum_avg = data["hum0"] + data["hum1"] + data["hum2"] + data["hum3"] + data["hum4"];
    hum_avg /= 5;
    console.log("Updating Hum");
    document.getElementById("hum_avg").innerHTML = hum_avg;
    document.getElementById("hum_0").innerHTML = data["hum0"];
    document.getElementById("hum_1").innerHTML = data["hum1"];
    document.getElementById("hum_2").innerHTML = data["hum2"];
    document.getElementById("hum_3").innerHTML = data["hum3"];
    document.getElementById("hum_4").innerHTML = data["hum4"];
}

function readLight() {
    console.log("Updating Light");
    document.getElementById("lit").innerHTML = data["lit"];
}

function readDate() {
    console.log("Updating Date");
    document.getElementById("created").innerHTML = data["created"];
}

function gotoMain() {
    document.location.href = "caretop_main.html";
}
function gotoQuick() {
    document.location.href = "caretop_quick.html";
}
function gotoSettings() {
    document.location.href = "caretop_settings.html";
}
function gotoHistory() {
    document.location.href = "caretop_history.html";
}
function gotoAccount() {
    document.location.href = "caretop_account.html";
}

function gotoMain1() {
    document.location.href = "../../caretop_main.html";
}
