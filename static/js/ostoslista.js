
var URL="yourdesiredURLfortxtfile"
function readFromFile()
{
    xmlhttp = new XMLHttpRequest()
    xmlhttp.open("GET", URL, false)
    xmlhttp.send(null)
    var filecontent = xmlhttp.responseText
    filelines=filecontent.split("\r\n")
    console.log(filelines)
    document.getElementById('list').innerHTML = filelines
}

