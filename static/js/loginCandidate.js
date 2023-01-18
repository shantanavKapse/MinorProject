function eyeToggle() {
    const x = document.querySelector("#passwrd");
    const icon = document.querySelector(".eye-icon");
    if (x.type === "password") {
        x.type = "text";
        icon.className = "eye-icon fa fa-eye-slash";
    } else {
        x.type = "password";
        icon.className = "eye-icon fa fa-eye";
    }
}