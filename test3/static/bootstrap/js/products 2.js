
$.cookie.json=true;
var products = [
    {
        "id": "1",
        "title": "Duralast\" Brake Pads ",
        "description": "Part Number:\"D1293" ,
        "specifications": {"Brand " : " Duralast ", " Location " : " Front ", " Warranty " : " Limited Lifetime"},
        "stockQty": 5,
        "price": 26.99,
        "currency": "$",
        "rating": 5,
        "images": [
            {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/epa/MKD908/image/4/",
                "caption": "",
                "isMain": 1
            }, {
                "src": "https://images-na.ssl-images-amazon.com/images/I/714DDJEzY9L._SL1500_.jpg",
                "caption": "side picture",
                "isMain": 0
            }]
    },
    {
        "id": "2",
        "title": "TRW Premium\" Brake Pads ",
        "description": "Part Number:\"TPC1293",
        "specifications": {"Brand": " TRW Premium", "Location": " Back", "Warranty": " Limited Lifetime"},
        "stockQty": 5,
        "price": 76.99,
        "currency": "$",
        "rating": 5,
        "images": [
            {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/trw/TPC0908/image/4/",
                "caption": "",
                "isMain": 1
            }, {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/trw/TPC0908/image/4/",
                "caption": "side picture",
                "isMain": 0
            }
        ]
    }
];

var battries = [
    {
        "id": "1",
        "title": "Duralast\" Battery ",
        "description": "Part Number:\"35S-DLG" ,
        "specifications": {"Brand " : " Duralast ", " Warranty " : " 5 years"},
        "stockQty": 5,
        "price": 133.99,
        "currency": "$",
        "rating": 5,
        "images": [
            {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/jci/35S-DLG/image/4/",
                "caption": "",
                "isMain": 1
            }, {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/jci/35S-DLG/image/4/",
                "caption": "side picture",
                "isMain": 0
            }]
    },
    {
        "id": "2",
        "title": "Odyssey \" Battery ",
        "description": "Part Number:\" 0750-2060",
        "specifications": {"Brand": " Odyssey ", "Warranty": " 3 years"},
        "stockQty": 5,
        "price": 239.99,
        "currency": "$",
        "rating": 5,
        "images": [
            {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/ody/0750-2060/image/4/",
                "caption": "",
                "isMain": 1
            }, {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/ody/0750-2060/image/4/",
                "caption": "side picture",
                "isMain": 0
            }]
    },

];


var lights = [
    {
        "id": "1",
        "title": "SilverStar Ultra \" Headlight ",
        "description": "Part Number:\"9006SU-2" ,
        "specifications": {"Brand " : " SilverStar Ultra ", " Warranty " : " Non "},
        "stockQty": 5,
        "price": 19.99,
        "currency": "$",
        "rating": 5,
        "images": [
            {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/syl/9006SU-2/image/4/",
                "caption": "",
                "isMain": 1
            }, {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/syl/9006SU-2/image/4/",
                "caption": "side picture",
                "isMain": 0
            }]
    },
    {
        "id": "2",
        "title": "SilverStar zXe \" Headlight ",
        "description": "Part Number:\" 9005SZ-2 ",
        "specifications": {"Brand": " SilverStar ", "Warranty": " Non"},
        "stockQty": 5,
        "price": 22.99,
        "currency": "$",
        "rating": 5,
        "images": [
            {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/syl/9005SZ-2/image/4/",
                "caption": "",
                "isMain": 1
            }, {
                "src": "http://contentinfo.autozone.com/znetcs/product-info/en/US/syl/9005SZ-2/image/4/",
                "caption": "side picture",
                "isMain": 0
            }]
    },

];

var users=[ {

    "uid": 100,

    "gid": 100,

    "fname": "John",

    "lname": "Smith",

    "email": "user@abcd.com",

    "isActive":1,

    "isLocked":0,

    "avatar": "https://secure.gravatar.com/avatar/be1d570665857e8384f874525a8fc755?s=50&d=https%3A%2F%2Fmycanvas.cau.edu%2Fimages%2Fmessages%2Favatar-50.png",

    "passwd": "s3cr3t",

    "shipTo": {

        "name": "Jane Smith",

        "address": "123 Maple Street",

        "city": "Pretendville",

        "state": "NY",

        "zip": "12345"

    },

    "billTo": {

        "name": "John Smith",

        "address": "123 Maple Street",

        "city": "Pretendville",

        "state": "NY",

        "zip": "12345"

    }

},{

    "uid": 101,

    "gid": 200,

    "fname": "John",

    "lname": "Admin",

    "email": "admin@abcd.com",

    "isActive":1,

    "isLocked":0,

    "avatar": "https://secure.gravatar.com/avatar/be1d570665857e8384f874525a8fc755?s=50&d=https%3A%2F%2Fmycanvas.cau.edu%2Fimages%2Fmessages%2Favatar-50.png",

    "passwd": "s3cr3t",

    "shipTo": {

        "name": "Jane Smith",

        "address": "123 Maple Street",

        "city": "Pretendville",

        "state": "NY",

        "zip": "12345"

    },

    "billTo": {

        "name": "John Smith",

        "address": "123 Maple Street",

        "city": "Pretendville",

        "state": "NY",

        "zip": "12345"

    }

}];

function displayProducts(){

    $.each(products,function (k,v){

        var prod = '<div id="" class="product">'+
            '<img  class="productImg" src="'+v.images[0].src+'"/><br/>'+
            '<span>Title:</span><span>'+v.title+'</span><br/>'+
            '<span>price:</span><span>$'+v.price +'</span><br/>';

        var specs="";
        $.each(v.specifications, function(sk,sv){
            specs+= sk+':'+sv+'|';
        })
        prod +='<span>Specs:</span><span class="spec">'+specs+'</span><br/>'
        prod += ' <input type="number" max="10" value="1"/>';
        prod += ' <button  onclick="addProductToShoppingCart('+v.id+',$(this).prev().val())'+'" >Add</button>';
        prod +='</div>';

        $('#productList').append(prod);
    });
}

function displayLight(){

    $.each(lights,function (k,v){

        var prod = '<div id="" class="product">'+
            '<img  class="productImg" src="'+v.images[0].src+'"/><br/>'+
            '<span>Title:</span><span>'+v.title+'</span><br/>'+
            '<span>price:</span><span>$'+v.price +'</span><br/>';

        var specs="";
        $.each(v.specifications, function(sk,sv){
            specs+= sk+':'+sv+'|';
        })
        prod +='<span>Specs:</span><span class="spec">'+specs+'</span><br/>'
        prod += ' <input type="number" max="10" value="1"/>';
        prod += ' <button  onclick="addProductToShoppingCart('+v.id+',$(this).prev().val())'+'" >Add</button>';
        prod +='</div>';

        $('#lights').append(prod);
    });
}

function displayBattries(){

    $.each(battries,function (k,v){

        var prod = '<div id="" class="product">'+
            '<img  class="productImg" src="'+v.images[0].src+'"/><br/>'+
            '<span>Title:</span><span>'+v.title+'</span><br/>'+
            '<span>price:</span><span>$'+v.price +'</span><br/>';

        var specs="";
        $.each(v.specifications, function(sk,sv){
            specs+= sk+':'+sv+'|';
        })
        prod +='<span>Specs:</span><span class="spec">'+specs+'</span><br/>'
        prod += ' <input type="number" max="10" value="1"/>';
        prod += ' <button  onclick="addProductToShoppingCart('+v.id+',$(this).prev().val())'+'" >Add</button>';
        prod +='</div>';

        $('#battries').append(prod);
    });
}

$(document).ready(function(){
    displayProducts();
    displayBattries();
    displayLight();
});

function addProductToShoppingCart(pid,qty){

    var selectedProduct;
    $.each(products,function (k,v) {
        if(v.id== pid){
            selectedProduct = v;
            return;
        }
    });

    if(!selectedProduct || isNaN(qty) || !parseInt(qty) ){
        return;
    }

    // check for the existing product
    var product = {"pid":selectedProduct.id,"price":selectedProduct.price,"qty":qty};
    var isDuplicate = lookupInCookieById(pid);

    if($.cookie("selectedItems")){
        var items = $.cookie("selectedItems");
        if(isDuplicate) {
            lookupUpdateQtyInCookieById(pid, qty);
        }else{
            items.push(product);
            $.cookie("selectedItems", items);
        }

    }else{
        $.cookie("selectedItems",[product]);
    }
}

function lookupInCookieById(id){
    var items = $.cookie("selectedItems");
    var found =false;
    if(!items){
        return false;
    }
    $.each(items,function (k,v){
        if(v.pid==id){
            found=true;
            return;
        }
    });
    return found;
}

function lookupUpdateQtyInCookieById(id,qty){
    var items = $.cookie("selectedItems");
    var found =0;
    $.each(items,function (k,v){
        if(v.pid==id){
            v.qty = parseInt(qty)+ parseInt(v.qty);
            return;
        }
    });
    $.cookie("selectedItems",items);
    return;
}
function displayCart(){

    var cartItems = $.cookie("selectedItems");
    var cartDisplay = '<table><caption>Shopping Cart</caption><thead><tr><th>Item Description</th><th>qty</th><th>Unit Price</th><th>Total</th></tr></thead><tbody>';
    var total =0;

    if(!cartItems || !cartItems.length) {
        $("#checkout").html('Shoping cart is empty!<br/><hr/>');
        return;
    }

    $.each(cartItems,function (k,v) {

        var pid = v.pid;
        var qty = v.qty;
        var sp;
        $.each(products,function (pk,pv) {
            if(pid==pv.id){
                sp= pv;
                return;
            }
        });
        var price = parseFloat(sp.price);
        cartDisplay += '<tr><td>' + sp.title + ' - ' + sp.description + '</td><td>' + qty + '</td>' +
            '<td>$' + price + '</td><td>$' + price* parseInt(qty) + '</td>' +
            '</tr>';
        total += price* parseInt(qty);
    });
    cartDisplay += '</tbody><tfoot><tr><th colspan="3">Grand Total</th><th>$' + parseFloat(total,2) + '</th></tr></tfoot></table>';
    $("#checkout").html(cartDisplay);
}
function displayCartItemCount(){
    var items = $.cookie("selectedItems");
    if(items ) {
        $('#cartCount').text(items.length);
    }else{
        $('#cartCount').text(0);
    }
}
$(document).ready(function () {

    displayCart();
    $('#emptyCart').click(function () {
        $.removeCookie("selectedItems");
        displayCart();
        return;
    });
    displayCartItemCount();

    $('#login').click(authenticate);
    $('#logout').click(logout);
});
