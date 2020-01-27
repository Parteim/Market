function sum_of_price(){
  let list_of_product = document.querySelectorAll('.cart_product_price');
  let sum_of_price = document.getElementById('sum_of_price');
  let sum = 0;

  list_of_product.forEach((item, index) => {
    sum += parseInt((item.children[0].innerText))
    console.log(sum);
  });

  sum_of_price.innerText = sum;

}

sum_of_price();
