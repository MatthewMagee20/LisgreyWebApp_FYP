document.addEventListener("DOMContentLoaded", function() {
    let els = document.getElementsByClassName("quantity");

    for(let i = 0; i < els.length; i++){
        els[i].addEventListener("keyup", function (){
            console.log(els[i].value);
            els[i].value = check(els[i].value);
        })
    }
})

function increaseQuantity(selected)
{
    let card = selected.parentElement;
    let quantity = card.getElementsByClassName("quantity")[0];

    quantity.value = parseInt(quantity.value) + 1;
}

function decreaseQuantity(selected)
{
    let card = selected.parentElement;
    let quantity = card.getElementsByClassName("quantity")[0];

    quantity.value = check(parseInt(quantity.value) - 1);
}

function check(val){
    if(val < 0 || val === undefined){
        val = 0;
        return val;
    }
    else{
        return val;
    }
}
