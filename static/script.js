function uppdateraKlocka() {
    var nu = new Date(); // Hämtar aktuell tid
    var timmar = nu.getHours(); // Hämtar timmar
    var minuter = nu.getMinutes(); // Hämtar minuter
    var sekunder = nu.getSeconds(); // Hämtar sekunder

    // Lägger till en nolla framför om siffran är mindre än 10
    timmar = (timmar < 10 ? "0" : "") + timmar;
    minuter = (minuter < 10 ? "0" : "") + minuter;
    sekunder = (sekunder < 10 ? "0" : "") + sekunder;

    // Uppdaterar textinnehållet i klockdiven med den nya tiden
    document.getElementById('digitalKlocka').textContent = timmar + ":" + minuter + ":" + sekunder;

    // Upprepar funktionen varje sekund
    setTimeout(uppdateraKlocka, 1000);
}

// Kallar på funktionen när sidan laddas
uppdateraKlocka();
