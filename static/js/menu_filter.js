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

// $(document).ready(function() {
//     $('.multiple_select').select2();
// });

// function submit() {
//     const tab = document.getElementsByClassName("tab-pane fade active show");
//     const values = $('#multiple_select_filter').val();
//     const card = tab[0].getElementsByClassName("card");
//
//     for(let i = 0; i < card.length; i++) {
//         const allergens = card[i].getElementsByClassName("card_allergens")[0].innerText;
//         const array = allergens.split(" ");
//
//         for(let j = 0; j < array.length; j++){
//             console.log(array[j]);
//             for(let x = 0; x < values.length; x++){
//                 if(array[j] === values[x]){
//                     console.log("yuppa");
//                     card[i].style.display = "none";
//                 }
//                 else{
//                     console.log("neg");
//                     card[i].style.display = "";
//                 }
//             }
//         }
//     }
//
// }

