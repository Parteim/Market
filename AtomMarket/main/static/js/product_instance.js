
function counterOfProduct() {
  var countUpBtn = document.getElementById('count_btn_up');
  var countDownBtn = document.getElementById('count_btn_down');
  var countField = document.getElementById('count_of_things');

  countUpBtn.addEventListener('click', () => {
    countField.value = parseInt(countField.value) + 1;
  });

  countDownBtn.addEventListener('click', () => {
    if(parseInt(countField.value) <= parseInt(countField.min)) {
      countField.value = countField.min;
      console.log("i'm hete")
    }
    else {
      countField.value = parseInt(countField.value) - 1;
    }
    

  });

}

counterOfProduct()