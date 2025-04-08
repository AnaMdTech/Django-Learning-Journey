function openDeleteModal(taskId) {
  const modal = document.getElementById("deleteModal");
  const form = document.getElementById("deleteForm");
  form.action = `/delete/${taskId}/`; // Make sure this URL pattern matches your urls.py
  modal.classList.remove("hidden");
}

function closeDeleteModal() {
  document.getElementById("deleteModal").classList.add("hidden");
}
