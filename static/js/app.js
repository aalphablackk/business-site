
document.addEventListener("DOMContentLoaded", () => {
    const backToTop = document.querySelector(".back-to-top");

    if (backToTop) {
        backToTop.addEventListener("click", (event) => {
            event.preventDefault();
            window.scrollTo({
                top: 0,
                behavior: "smooth",
            });
        });
    }
});
