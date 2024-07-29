function AddProductBasketBuy(product) {
    $.get('/cart/add-product-basketbuy/',{
        'product_id':product,
    }).then(
        res=>{
            return res
        }
        )
}
