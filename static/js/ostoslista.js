function readFromFile()
{
    let ipfromconfig = "";
    fetch("config.json")
        .then (response => response.json())
        .then((json) => {
            ipfromconfig = json.ipaddress;
            
            console.log(ipfromconfig)
            xmlhttp = new XMLHttpRequest()
            xmlhttp.open("GET", ipfromconfig, false)
            xmlhttp.send(null)
            var filecontent = xmlhttp.responseText
            filelines=filecontent.split("\r\n")
            console.log(filelines)
            document.getElementById('list').innerHTML = filelines
            });
        
   
}

