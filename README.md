# 📒 Contact Book

A modern, GUI-based contact management application built with **Python** and **Tkinter**. Features a sleek dark-themed interface inspired by the **Catppuccin Mocha** color palette.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ➕ **Add Contact** | Save new contacts with name, phone, email, and address |
| ✏️ **Edit Contact** | Update any existing contact's details |
| 👁️ **View Contact** | View full details of a selected contact in a popup |
| 🗑️ **Delete Contact** | Remove contacts with a confirmation prompt |
| 🔍 **Real-time Search** | Instantly filter contacts by name or phone number as you type |
| 💾 **Persistent Storage** | All contacts are saved locally in `contacts.json` |

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Core programming language |
| **Tkinter** | GUI framework for the desktop interface |
| **JSON** | Lightweight data storage for contacts |

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+** installed on your system
- **Tkinter** (comes pre-installed with Python on most systems)

> **Note:** No external dependencies or `pip install` required — the app uses only Python's built-in standard library.

### Run the Application

```bash
python contact_book_.py
```

---

## 🎨 User Interface

The application features a polished **dark theme** with color-coded action buttons:

| Button | Color | Action |
|--------|-------|--------|
| ＋ Add | 🟢 Green (`#a6e3a1`) | Opens a form to add a new contact |
| ✏ Edit | 🔵 Blue (`#89b4fa`) | Opens a form to edit the selected contact |
| 👁 View | 🟡 Yellow (`#f9e2af`) | Shows full details of the selected contact |
| 🗑 Delete | 🔴 Red (`#f38ba8`) | Deletes the selected contact after confirmation |

### Theme Colors

| Element | Color Code | Usage |
|---------|------------|-------|
| Background | `#1e1e2e` | Main window background |
| Surface | `#313244` | Search bar, list items, input fields |
| Text | `#cdd6f4` | Primary text color |
| Accent | `#89b4fa` | Selection highlight, save buttons |

---

## 📂 Project Structure

```
codsoft/
├── contact_book_.py    # Main application source code
├── contacts.json       # Auto-generated contact data storage
└── README.md           # Project documentation
```

---

## 📖 How It Works

1. **Launch** — Run the script to open the Contact Book window.
2. **Add** — Click the **＋ Add** button to open a form. Fill in the name (required), phone (required), email, and address fields, then click **Save**.
3. **Search** — Type in the search bar to instantly filter contacts by name or phone number.
4. **Edit** — Select a contact from the list, then click **✏ Edit** to modify its details.
5. **View** — Select a contact and click **👁 View** to see all stored details in a popup.
6. **Delete** — Select a contact and click **🗑 Delete**. Confirm the deletion in the dialog that appears.

All changes are automatically saved to `contacts.json` in the same directory.

---

## 👤 Author

**Your Name**
- CodSoft Internship — Python Programming
- GitHub: [@your-username](https://github.com/your-username)

---

## 📄 License

This project is developed as part of the **CodSoft Internship** program and is available for educational purposes.
