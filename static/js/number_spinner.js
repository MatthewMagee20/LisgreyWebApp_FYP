function hello(selected)
{
    let card = selected.parentElement;
    const quantity = card.getElementsByClassName("quantity")[0].value;
    console.log(quantity);
}