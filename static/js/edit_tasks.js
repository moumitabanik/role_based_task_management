// call back to get datatable reference
let tableFunRef;
const getTableRef = (dataTableRefresh) => {
    dataTableRefresh();
};

const cancelButton = document.getElementById("cancel_editTask_popup");
const saveButton = document.getElementById("save_editTask_popup");
const popup = document.getElementById("editTask_popup");

const openTaskEditModal = (rowData, dataTableRefresh) => {
    tableFunRef = dataTableRefresh;
    // Assuming 'editEditForm' is defined elsewhere
    editEditForm.reset();
    popup.style.display = "flex";

    function setValuesToForm(rowData) {
        document.querySelector("#editEditForm input[name='name']").value = rowData.name;
        document.querySelector("#editEditForm textarea[name='description']").value = rowData.description;
        document.querySelector("#editEditForm select[name='assigned_to']").value = rowData.assigned_to;
        document.querySelector("#editEditForm input[name='status']").value = rowData.status;
        document.querySelector("#editEditForm input[name='deadline']").value = getFormattedDate(rowData.deadline);
        document.querySelector("#editEditForm input[name='created_by']").value = rowData.created_by;
        document.querySelector("#editEditForm select[name='project']").value = rowData.project;
    }

    setValuesToForm(rowData);
    console.log(saveButton)
    saveButton.addEventListener("click", async (e) => {
        console.log("sdjbfsjfb")
        e.preventDefault();

        const taskData = {
            name: document.querySelector("#editEditForm input[name='name']").value,
            description: document.querySelector("#editEditForm textarea[name='description']").value,
            status: document.querySelector("#editEditForm input[name='status']").value,
            deadline: document.querySelector("#editEditForm input[name='deadline']").value,
            created_by: document.querySelector("#editEditForm input[name='created_by']").value,
        };

        let taskId = rowData.id; // Assuming the task ID is stored in the 'id' property of the rowData object

        let edtres = await taskEditCall(taskData, taskId);
        if (edtres === "success") {
            popup.style.display = "none";
            dataTableRefreshStore();
        } else {
            alert(edtres);
        }
        getTableRef(tableFunRef);
    }, { once: true });
};

cancelButton.addEventListener("click", () => {
    // resetFields();
    popup.style.display = "none";
    editEditForm.reset();
    getTableRef(tableFunRef);
});

const taskEditCall = async (taskData, taskId) => {
    try {
        const response = await fetch(
            `${base_url}/projects/tasks/${taskId}/update/`, // Include task ID in the URL
            {
                method: "PATCH", // Assuming you are using PATCH method to update
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
