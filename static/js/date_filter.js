function filterDate(){
    let date = document.getElementById("date").value;
    let reservation_table = document.getElementById("reservation_table");

    for (let i = 1; reservation_table.rows[i]; i++) {
        const row = reservation_table.rows[i]
        if(row.cells[2].innerText === date){
            row.style.display = "";
        }
        else{
            row.style.display = "none";
        }
    }
}

function reset(){
    let reservation_table = document.getElementById("reservation_table");

    for (let i = 1; reservation_table.rows[i]; i++) {
        reservation_table.rows[i].style.display = "";
    }
}
