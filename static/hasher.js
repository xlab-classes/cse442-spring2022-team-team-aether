
function createSubmit(){
    var formData = new FormData();
    let form1 = document.getElementById("createaccount");
    var x = form.elements["Password"];
    formData.append("Username", form1.elements["Username"]);
    formData.append("Password", x);
    formData.submit();
}