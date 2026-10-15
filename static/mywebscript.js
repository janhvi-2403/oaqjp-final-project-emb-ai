function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const resultElement = document.getElementById("system_response");

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            resultElement.textContent = this.responseText;
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" +
            encodeURIComponent(textToAnalyze),
        true
    );
    xhttp.send();
}
