let dataTableRefreshStore;
const getTableRefAdd = (dataTableRefresh) => {
    dataTableRefreshStore = dataTableRefresh;
}

document.addEventListener("DOMContentLoaded", function () {
    const addProjectButton = document.getElementById("addProject");
    const popup = document.getElementById("addproject_popup");
    const cancelButton = document.getElementById("cancel_addproject_popup");
    const saveButton = document.getElementById("save_addproject_popup");

    if (addProjectButton) {
        addProjectButton.addEventListener("click", () => {
            popup.style.display = "flex";
        });
    }

    if (cancelButton) {
        cancelButton.addEventListener("click", () => {
            // Optionally reset form fields here
            popup.style.display = "none";
        });
    }

    if (saveButton) {
        saveButton.addEventListener("click", async (e) => {
            e.preventDefault();

            const Projectname = document.querySelector("#ProjectCreateForm input[name='name']").value;
            const description = document.querySelector("#ProjectCreateForm textarea[name='description']").value;
            const status = document.querySelector("#ProjectCreateForm select[name='status']").value;
            
            const ProjectData = {
                name: Projectname,
                description: description,
                status: status
            };

            let res = await ProjectAddCall(ProjectData);

            if (res === "success") {
                popup.style.display = "none";
                dataTableRefreshStore();
            } else {
                alert(res);
            }
        });
    }
});

const ProjectAddCall = async (ProjectData) => {
    try {
        const response = await fetch(
            `${base_url}/projects/projects/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                },
                body: JSON.stringify(ProjectData),
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
