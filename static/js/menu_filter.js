function filter_menu() {
    const input = document.getElementById("filter_input").value.toUpperCase();
    const card = document.getElementsByClassName("card");

    for(let i = 0; i < card.length; i++){
        const card_title = card[i].getElementsByClassName("card_title")[0];

        if(card_title){
            const value = card_title.innerText.toUpperCase();
            if(value.indexOf(input) > -1){
                card[i].style.display = "";
            }
            else{
                card[i].style.display = "none";
            }
        }
    }
}

function submit() {
    const tab = document.getElementsByClassName("tab-pane fade active show");
    let values = $('.selectpicker').val();
    const card = tab[0].getElementsByClassName("card");

    // Reset cards if array is empty
    if(values === null){
        values = [""]
    }

    for(let i = 0; i < card.length; i++) {
        const allergens = card[i].getElementsByClassName("card_allergens")[0].innerText;
        const array = allergens.split(", ");

        if(values.some((val) => array.indexOf(val) !== -1)){
            card[i].style.display = "none";
        }
        else if(!values.length){
            card[i].style.display = "";
        }
        else {
            card[i].style.display = "";
        }
    }
}

