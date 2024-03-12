function toggleMenu() {
    let menuList = document.getElementById("menuList");
    if (menuList.style.display === "none") {
        menuList.style.display = "block";
    } else {
        menuList.style.display = "none";
    }
}
const headerEl = document.getElementById("header")
window.addEventListener("scroll",function(){
 const scrollPos = window.scrollY

 if(scrollPos>100){
    headerEl.classList.add("header-mini")
 }else{
    headerEl.classList.remove("header-mini")
 }
}
)