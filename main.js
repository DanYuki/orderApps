var menuList = {
    "Item 1" : 8000,
    "Item 2": 9000
}
var pairedOrder = {}

function quantityModifier(opt, entryId) {
    if(opt == "+"){
        let value = document.getElementById(entryId).value;
        value = parseInt(value);
        value += 1;
        document.getElementById(entryId).value = value;
    }
    else if(opt == "-"){
        let value = document.getElementById(entryId).value;
        value = parseInt(value);
        value -= 1;
        document.getElementById(entryId).value = value;
    }
}

function addToCart(entryId, itemName){
    if(pairedOrder[itemName] > 0){
        let Q = document.getElementById(entryId).value;
        Q = parseInt(Q)
        pairedOrder[itemName] += Q;
        document.getElementById(entryId).value = 0;
    }
    else{
        let Q = document.getElementById(entryId).value;
        Q = parseInt(Q)
        pairedOrder[itemName] = Q;
        document.getElementById(entryId).value = 0;
    }
}

function showItems(){
    let text=""
    for(x in pairedOrder){
        text += `- ${x}(${pairedOrder[x]}) = Rp.${pairedOrder[x] * menuList[x]} \n`
    }
    document.getElementById("item-list").innerText = text;
}