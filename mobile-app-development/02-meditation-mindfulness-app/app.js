// Meditation & Mindfulness App — Interactive Application Logic (localStorage persisted)
const STORAGE_KEY = "riseahead_meditation_mindfulness_app";
let items = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null") || [
  { id: 1, title: "Initial Workspace Entry", status: "Active", created: new Date().toLocaleDateString() },
  { id: 2, title: "Sample Workflow Record", status: "Completed", created: new Date().toLocaleDateString() },
];

function save() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
}

function render() {
  const list = document.getElementById("list");
  const q = (document.getElementById("search").value || "").toLowerCase();
  const filtered = items.filter((it) => it.title.toLowerCase().includes(q));
  document.getElementById("count").textContent = `${filtered.length} / ${items.length} items`;
  list.innerHTML = filtered.map((it) => `
    <div class="row">
      <div>
        <strong>${it.title}</strong>
        <div class="meta">${it.status} • ${it.created}</div>
      </div>
      <div class="actions">
        <button onclick="toggleItem(${it.id})">Toggle</button>
        <button class="danger" onclick="removeItem(${it.id})">Delete</button>
      </div>
    </div>
  `).join("") || '<p class="meta">No records match your filter.</p>';
}

function addItem() {
  const input = document.getElementById("newTitle");
  const val = input.value.trim();
  if (!val) return;
  items.unshift({ id: Date.now(), title: val, status: "Active", created: new Date().toLocaleDateString() });
  input.value = "";
  save();
  render();
}

function toggleItem(id) {
  const it = items.find((x) => x.id === id);
  if (it) it.status = it.status === "Active" ? "Completed" : "Active";
  save();
  render();
}

function removeItem(id) {
  items = items.filter((x) => x.id !== id);
  save();
  render();
}

document.getElementById("addBtn").addEventListener("click", addItem);
document.getElementById("search").addEventListener("input", render);
render();
