const quickSearchForm = document.getElementById("quick-search-form");
const quickSearchResult = document.getElementById("quick-search-result");

if (quickSearchForm && quickSearchResult) {
  quickSearchForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const matriculeInput = document.getElementById("matricule");
    const matricule = matriculeInput ? matriculeInput.value.trim() : "";

    if (!matricule) {
      quickSearchResult.innerHTML = '<div class="alert alert-error">Please enter a matricule.</div>';
      return;
    }

    quickSearchResult.innerHTML = '<div class="alert alert-success">Searching...</div>';

    try {
      const response = await fetch(`/ajax/student/${encodeURIComponent(matricule)}`);
      const payload = await response.json();

      if (!payload.success) {
        quickSearchResult.innerHTML = `<div class="alert alert-error">${payload.message}</div>`;
        return;
      }

      const student = payload.data;
      quickSearchResult.innerHTML = `
        <div class="card">
          <h2>${student.name}</h2>
          <p><strong>Matricule:</strong> ${student.matricule}</p>
          <p><strong>Department:</strong> ${student.department}</p>
          <p><strong>Age:</strong> ${student.age}</p>
          <p><strong>English:</strong> ${student.english}</p>
          <p><strong>French:</strong> ${student.french}</p>
          <p><strong>Total marks:</strong> ${student.total_marks}</p>
          <p><strong>Average:</strong> ${student.average}</p>
          <p><strong>Grade:</strong> ${student.grade}</p>
          <a class="button button-secondary" href="/student/${student.matricule}/edit">Edit student</a>
        </div>
      `;
    } catch (error) {
      quickSearchResult.innerHTML = '<div class="alert alert-error">Unable to fetch student data.</div>';
    }
  });
}
