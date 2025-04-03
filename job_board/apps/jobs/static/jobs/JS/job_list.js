document.addEventListener("DOMContentLoaded", function () {
  const jobCategories = document.querySelectorAll(".job-category");
  let currentlyOpen = null;

  jobCategories.forEach((category) => {
    category.addEventListener("click", () => {
      const jobList = category.nextElementSibling;

      if (currentlyOpen && currentlyOpen !== jobList) {
        currentlyOpen.classList.remove("show");
      }

      jobList.classList.toggle("show");
      currentlyOpen = jobList.classList.contains("show") ? jobList : null;
    });
  });
});
