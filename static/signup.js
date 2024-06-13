const element = document.getElementsByTagName("input");
console.log(element)
for (let i = 0; i < element.length; i++) {
    console.log(element[i].classList.value)
    element[i].classList.value = "form-control"
  }