function getData(){
    let data  = [];
    let doc = document.querySelector('#tabs-sim-tt > div > div.sim-so__info.sim-number > table > tbody');
    let sdt_doc = doc.querySelectorAll('tr td:nth-child(2) span');
    sdt_doc.forEach(element => {
        data.push(element.textContent);
    });

    return data;
}

console.log(getData());
