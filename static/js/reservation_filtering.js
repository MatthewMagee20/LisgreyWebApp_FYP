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
    let date = document.getElementById("date").value;
    let reservation_table = document.getElementById("reservation_table");

    for (let i = 1; reservation_table.rows[i]; i++) {
        const row = reservation_table.rows[i]
        if(row.cells[4].innerText === date){
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }
    }
}

function filterByTime() {
    let time = document.getElementById("time").value;
    let reservation_table = document.getElementById("reservation_table");

    for (let i = 1; reservation_table.rows[i]; i++) {
        const row = reservation_table.rows[i]
        if(row.cells[5].innerText === time){
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }
    }
}

function filterByDateTime() {
    const date = document.getElementById("dt_date").value;
    const time = document.getElementById("dt_time").value;
    const reservation_table = document.getElementById("reservation_table");

    for (let i = 1; reservation_table.rows[i]; i++) {
        const row = reservation_table.rows[i]
        if ((row.cells[4].innerText === date) && (row.cells[5].innerText === time)) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    }
}

function reset() {
    let reservation_table = document.getElementById("reservation_table");

    for (let i = 1; reservation_table.rows[i]; i++) {
        reservation_table.rows[i].style.display = "";
    }
}
