function startBot() {
    fetch('/start-bot')
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error('Error:', error));
}
