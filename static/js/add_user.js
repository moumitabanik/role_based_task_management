

let dataTableRefreshStore;
const getTableRefAdd =(dataTableRefresh)=>{
 dataTableRefreshStore = dataTableRefresh
}
document.addEventListener("DOMContentLoaded", function () {
 const addUser = document.querySelectorAll("#addUser");
 const popup = document.querySelectorAll("#addUser_popup");
 const cancelButton = document.querySelectorAll("#cancel_addUser_popup");
 const saveButton = document.querySelectorAll("#save_addUser_popup");


 for (let i = 0; i < addUser.length; i++) {
   addUser[i].addEventListener("click", () => {
     popup[i].style.display = "flex";
   });
 }


 for (let i = 0; i < cancelButton.length; i++) {
   cancelButton[i].addEventListener("click", () => {
     // resetFields();
     popup[i].style.display = "none";
   });
 }
 for (let i = 0; i < saveButton.length; i++) {
    saveButton[i].addEventListener("click", async (e) => {
        e.preventDefault();

        const username = document.querySelector("#userCreateForm input[name='username']").value;
        const firstName = document.querySelector("#userCreateForm input[name='first_name']").value;
        const lastName = document.querySelector("#userCreateForm input[name='last_name']").value;
        const email = document.querySelector("#userCreateForm input[name='email']").value;
        const role = document.querySelector("#userCreateForm select[name='role']").value;
        const password = document.querySelector("#userCreateForm input[name='password']").value;

        const userData = {
            username: username,
            first_name: firstName,
            last_name: lastName,
            email: email,
            role: role,
            password: password
        };

        let res = await UserAddCall(userData);

        if (res === "success") {
            popup[i].style.display = "none";
            dataTableRefreshStore();
        } else {
            alert(res);
        }
    });
}
});

const UserAddCall = async (userData) => {
try {
    const response = await fetch(
        `${base_url}/dashboard/register/`,
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                Authorization: `Token ${localStorage.getItem("token")}`,
            },
            body: JSON.stringify(userData),
        }
    );
    if (response.ok) {
        return "success";
    } else {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Error occurred.");
    }
} catch (error) {
    console.error("Error:", error);
    return "Error!";
}
};