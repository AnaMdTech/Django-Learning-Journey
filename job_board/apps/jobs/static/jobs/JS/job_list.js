document.addEventListener("DOMContentLoaded", function () {
  const jobCategories = document.querySelectorAll(".job-category");

  jobCategories.forEach((category) => {
    category.addEventListener("click", () => {
      const jobList = category.nextElementSibling;
      jobList.classList.toggle("show");
    });
  });
});
