function addToBasket(selected){

    const id = selected.parentElement.parentElement;
    const itemName = id.getElementsByClassName("food-item-name")[0].innerText;
    const itemPrice = id.getElementsByClassName("food-item-price")[0].innerText;

    if (check(itemName)){
        updateQuantity(itemName);
        updatePrice(itemName);
    }

    else{
        const basketTable = document.getElementById("basket");
        const rowCount = basketTable.rows.length;
        const row = basketTable.insertRow(rowCount);
        const basketRowName = row.insertCell(0);
        const basketRowQuantity = row.insertCell(1);
        const basketRowPrice = row.insertCell(2)

        basketRowPrice.className = "basket-item-price";
        basketRowQuantity.className = "basket-item-quantity";
        basketRowName.className = "basket-item-name";

        basketRowName.innerText = itemName;
        basketRowPrice.innerText = "$"+itemPrice;
        basketRowQuantity.innerText = "1";
    }


}

function check(itemName){
    const basketTable = document.getElementById("basket");

    for(let i = 0; i < basketTable.rows.length; i++){
        if (basketTable.rows[i].cells[0].innerHTML === itemName){
            return true;
        }
    }
}

function updateQuantity(itemName)
{
    const basketTable = document.getElementById("basket");

    for(let i = 0; i < basketTable.rows.length; i++)
    {
        if (basketTable.rows[i].cells[0].innerHTML === itemName){
            const itemQuantity = basketTable.rows[i].getElementsByClassName("basket-item-quantity")[0];
            let quantity = Number(itemQuantity.innerText);
            quantity += 1;
            itemQuantity.innerText = quantity;
        }
    }
}


function updateItemPrice(){
    const basketTable = document.getElementById("basket");
    let total = 0;

    for(let i = 0; i < basketTable.rows.length; i++)
    {
        const itemPrice = basketTable.rows[i].getElementsByClassName("basket-item-price")[0];
        const itemQuantity = basketTable.rows[i].getElementsByClassName("basket-item-quantity")[0];
        const price = parseFloat(itemPrice.innerText.replace('$',''))
        const quantity = itemQuantity.value;

        total = (price * quantity);
    }
}
