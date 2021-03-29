function filterSelect() {
    const option = document.getElementById("filter_option").value;
    const dateDiv = document.getElementById("filter_by_date");
    const timeDiv = document.getElementById("filter_by_time");
    const dateTimeDiv = document.getElementById("filter_by_date_time");


    if (option === "1") {
        reset();
        dateDiv.style.display = "block";
        timeDiv.style.display = "none";
        dateTimeDiv.style.display = "none";

    }else if (option === "2") {
        reset();
        timeDiv.style.display = "block"
        dateDiv.style.display  = "none";
        dateTimeDiv.style.display = "none";

    }else {
        reset();
        dateTimeDiv.style.display = "block";
        timeDiv.style.display = "none"
        dateDiv.style.display  = "none";
    }
}

function filterByDate() {
    const activeTab = document.getElementsByClassName("tab-pane fade active show");
    const reservation_table = activeTab[0].getElementsByClassName("table");
    const date = document.getElementById("date").value;

    for (let i = 1; reservation_table[0].rows[i]; i++) {
        const row = reservation_table[0].rows[i]
        console.log(row);
        if(row.cells[3].innerText === date){
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }
    }
}

function filterByTime() {
    const activeTab = document.getElementsByClassName("tab-pane fade active show");
    const reservation_table = activeTab[0].getElementsByClassName("table");
    let time = document.getElementById("time").value;

    for (let i = 1; reservation_table[0].rows[i]; i++) {
        const row = reservation_table[0].rows[i]
        if(row.cells[4].innerText === time){
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }
    }
}

function filterByDateTime() {
    reset();
    const date = document.getElementById("dt_date").value;
    const time = document.getElementById("dt_time").value;
    const activeTab = document.getElementsByClassName("tab-pane fade active show");
    const reservation_table = activeTab[0].getElementsByClassName("table");

    console.log(date);
    console.log(time);
    for (let i = 1; reservation_table[0].rows[i]; i++) {
        const row = reservation_table[0].rows[i]
        if((row.cells[3].innerText === date) && (row.cells[4].innerText === time)){
            console.log(row.cells[3].innerText)
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }
    }
}

function reset() {
    const activeTab = document.getElementsByClassName("tab-pane fade active show");
    const reservation_table = activeTab[0].getElementsByClassName("table");

    for (let i = 1; reservation_table[0].rows[i]; i++) {
        reservation_table[0].rows[i].style.display = "";
    }
}