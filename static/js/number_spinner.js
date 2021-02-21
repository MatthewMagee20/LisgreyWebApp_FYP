function increaseQuantity(selected)
{
    let card = selected.parentElement;
    let quantity = card.getElementsByClassName("quantity")[0]; //1

    quantity.value = parseInt(quantity.value) + 1;
}

function decreaseQuantity(selected)
{
    let card = selected.parentElement;
    let quantity = card.getElementsByClassName("quantity")[0]; //1

    quantity.value = parseInt(quantity.value) - 1;
}