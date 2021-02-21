function filter_menu() {
    const input = document.getElementById("filter_input").value.toUpperCase();
    console.log(input);

    const card = document.getElementsByClassName("card");

    for(let i = 0; i < card.length; i++){
        const card_title = card[i].getElementsByClassName("card_title")[0];
        console.log(card_title);

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