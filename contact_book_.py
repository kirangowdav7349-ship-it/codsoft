import tkinter as tk
from tkinter import messagebox
import json, os

FILE = "contacts.json"

def load():
    return json.load(open(FILE)) if os.path.exists(FILE) else []

def save(contacts):
    json.dump(contacts, open(FILE, "w"), indent=2)

# ── App ──────────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x420")
root.config(bg="#1e1e2e")

contacts = load()

def refresh(filter_text=""):
    listbox.delete(0, tk.END)
    for c in contacts:
        if filter_text.lower() in c["name"].lower() or filter_text in c["phone"]:
            listbox.insert(tk.END, f"  {c['name']}  |  {c['phone']}")

def get_selected_index():
    sel = listbox.curselection()
    if not sel:
        messagebox.showwarning("Select", "Please select a contact first.")
        return None
    query = search_var.get()
    filtered = [c for c in contacts if query.lower() in c["name"].lower() or query in c["phone"]]
    return contacts.index(filtered[sel[0]])

def open_form(title, data=None, on_save=None):
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("340x280")
    win.config(bg="#1e1e2e")
    win.grab_set()

    fields = ["Name", "Phone", "Email", "Address"]
    entries = {}
    for i, f in enumerate(fields):
        tk.Label(win, text=f, bg="#1e1e2e", fg="#cdd6f4").grid(row=i, column=0, padx=14, pady=6, sticky="w")
        e = tk.Entry(win, bg="#313244", fg="#cdd6f4", insertbackground="white", relief="flat", width=28)
        e.grid(row=i, column=1, padx=10, pady=6)
        if data:
            e.insert(0, data.get(f.lower(), ""))
        entries[f.lower()] = e

    def submit():
        name = entries["name"].get().strip()
        phone = entries["phone"].get().strip()
        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone are required.", parent=win)
            return
        on_save({k: e.get().strip() for k, e in entries.items()})
        win.destroy()
        refresh(search_var.get())

    tk.Button(win, text="Save", command=submit, bg="#89b4fa", fg="#1e1e2e",
              relief="flat", width=10).grid(row=5, column=1, pady=14, sticky="e", padx=10)

def add_contact():
    open_form("Add Contact", on_save=lambda d: contacts.append(d) or save(contacts))

def edit_contact():
    idx = get_selected_index()
    if idx is None: return
    def do_edit(d):
        contacts[idx] = d
        save(contacts)
    open_form("Edit Contact", data=contacts[idx], on_save=do_edit)

def delete_contact():
    idx = get_selected_index()
    if idx is None: return
    if messagebox.askyesno("Delete", f"Delete '{contacts[idx]['name']}'?"):
        contacts.pop(idx)
        save(contacts)
        refresh(search_var.get())

def view_contact():
    idx = get_selected_index()
    if idx is None: return
    c = contacts[idx]
    messagebox.showinfo("Contact Details",
        f"Name:    {c['name']}\nPhone:   {c['phone']}\nEmail:   {c.get('email','—')}\nAddress: {c.get('address','—')}")

# ── UI Layout ─────────────────────────────────────────────────────────────────
tk.Label(root, text="📒 Contact Book", bg="#1e1e2e", fg="#cdd6f4",
         font=("Segoe UI", 16, "bold")).pack(pady=(14, 4))

# Search bar
search_var = tk.StringVar()
search_var.trace_add("write", lambda *_: refresh(search_var.get()))
sf = tk.Frame(root, bg="#313244")
sf.pack(fill="x", padx=16, pady=4)
tk.Label(sf, text="🔍", bg="#313244", fg="#6c7086").pack(side="left", padx=6)
tk.Entry(sf, textvariable=search_var, bg="#313244", fg="#cdd6f4",
         insertbackground="white", relief="flat").pack(fill="x", expand=True, pady=6)

# Listbox
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(fill="both", expand=True, padx=16, pady=6)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side="right", fill="y")
listbox = tk.Listbox(frame, bg="#313244", fg="#cdd6f4", selectbackground="#89b4fa",
                     selectforeground="#1e1e2e", relief="flat", font=("Segoe UI", 10),
                     yscrollcommand=scrollbar.set, activestyle="none")
listbox.pack(fill="both", expand=True)
scrollbar.config(command=listbox.yview)

# Buttons
bf = tk.Frame(root, bg="#1e1e2e")
bf.pack(pady=8)
for text, cmd, color in [
    ("＋ Add",    add_contact,    "#a6e3a1"),
    ("✏ Edit",   edit_contact,   "#89b4fa"),
    ("👁 View",  view_contact,   "#f9e2af"),
    ("🗑 Delete", delete_contact, "#f38ba8"),
]:
    tk.Button(bf, text=text, command=cmd, bg=color, fg="#1e1e2e",
              relief="flat", width=10, font=("Segoe UI", 9, "bold")).pack(side="left", padx=4)

refresh()
root.mainloop()
