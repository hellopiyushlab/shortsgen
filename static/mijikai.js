
function generate() {
    var text = document.getElementById('t1').value;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/generate', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 3 && xhr.status === 200) {
            var responseData = xhr.responseText;
            document.getElementById('t2').value = responseData;
        }
    };
    xhr.send(JSON.stringify({ 'text': text }));
}


function down() {
    window.location.href = "/download";
}