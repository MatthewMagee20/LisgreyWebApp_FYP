function addToBasket(selected)
{
    const itemDiv = selected.parentElement.parentElement;
    const itemName = itemDiv.getElementsByClassName("food-item-name")[0].innerText;
    const itemPrice = itemDiv.getElementsByClassName("food-item-price")[0].innerText;

    // check if item already in basket
    if (check(itemName))
    {
        updateQuantity(itemName);
        updateItemPrice(itemName);
    }

    else
    {
        const basketTable = document.getElementById("basket");
        const rowCount = basketTable.rows.length;
        const row = basketTable.insertRow(rowCount);
        const basketRowName = row.insertCell(0);
        const basketRowQuantity = row.insertCell(1);
        const basketRowPrice = row.insertCell(2)
        const basketRowTotalPrice = row.insertCell(3);

        row.setAttribute("id", "item-" + itemDiv.id);

        row.name = "item-" + itemDiv.id;

        console.log(row.name);


        basketRowName.className = "basket-item-name";
        basketRowQuantity.className = "basket-item-quantity";
        basketRowPrice.className = "basket-item-price";
        basketRowTotalPrice.className = "basket-item-total-price";

        basketRowName.innerText = itemName;
        basketRowPrice.innerText = itemPrice;
        basketRowQuantity.innerText = "1";

        updateItemPrice(itemName);
    }
}

// check if item already in basket
function check(itemName)
{
    const basketTable = document.getElementById("basket");

    for(let i = 0; i < basketTable.rows.length; i++)
    {
        if (basketTable.rows[i].cells[0].innerHTML === itemName)
        {
            return true;
        }
    }
}

// update quantity field for item
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

// update price for item and total basket
function updateItemPrice(itemName)
{
    const basketTable = document.getElementById("basket");
    let itemTotal = 0;
    let basketTotal = 0;

    for (let i = 0; i < basketTable.rows.length; i++)
    {
        if (basketTable.rows[i].cells[0].innerHTML === itemName)
        {
            let itemPrice = basketTable.rows[i].getElementsByClassName("basket-item-price")[0];
            let itemQuantity = basketTable.rows[i].getElementsByClassName("basket-item-quantity")[0];
            let itemPriceTotal = basketTable.rows[i].getElementsByClassName("basket-item-total-price")[0];
            let overall = document.getElementById("basket-total-price");
            let current_price = parseFloat(overall.innerText);

            // update price for items x quantity
            itemTotal = parseFloat(itemPrice.innerText) * parseInt(itemQuantity.innerText);
            itemPriceTotal.innerText = ""+ itemTotal;

            // update basket total price
            basketTotal = current_price + itemTotal;
            overall.innerHTML = ""+basketTotal
        }
    }
}