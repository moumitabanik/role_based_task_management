let dataTableRefreshStore;
const getTableRefAdd = (dataTableRefresh) => {
    dataTableRefreshStore = dataTableRefresh;
}
const getFormattedDate = (dateString) => {
    const date = new Date(dateString);
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');
    return `${year}-${month}-${day}`;
};
document.addEventListener("DOMContentLoaded", function () {
    const addTaskButton = document.getElementById("addTask");
    const popup = document.getElementById("addTask_popup");
    const cancelButton = document.getElementById("cancel_addTask_popup");
    const saveButton = document.getElementById("save_addTask_popup");

    if (addTaskButton) {
        addTaskButton.addEventListener("click", () => {
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

            const taskname = document.querySelector("#taskCreateForm input[name='name']").value;
            const description = document.querySelector("#taskCreateForm textarea[name='description']").value;
            const assignedTo = document.querySelector("#taskCreateForm select[name='assigned_to']").value;
            const status = document.querySelector("#taskCreateForm input[name='status']").value;
            const deadline = getFormattedDate(document.querySelector("#taskCreateForm input[name='deadline']").value);
            const createdBy = document.querySelector("#taskCreateForm input[name='created_by']").value;
            const project = document.querySelector("#taskCreateForm select[name='project']").value;

            const taskData = {
                name: taskname,
                description: description,
                assigned_to: assignedTo,
                project: project,
                status: status,
                deadline: deadline,
                created_by: createdBy
            };

            let res = await taskAddCall(taskData);

            if (res === "success") {
                popup.style.display = "none";
                dataTableRefreshStore();
            } else {
                alert(res);
            }
        });
    }
});

const taskAddCall = async (taskData) => {
    try {
        const response = await fetch(
            `${base_url}/projects/tasks-add/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                },
                body: JSON.stringify(taskData),
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
