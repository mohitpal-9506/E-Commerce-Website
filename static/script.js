let buttons =
document.querySelectorAll("button");

buttons.forEach(btn=>{
    btn.addEventListener("click",()=>{
        alert("Product Added To Cart");
    });
});
