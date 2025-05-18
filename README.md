# A2UWID

## UWorld ID Extractor for Anki

![Anki Version](https://img.shields.io/badge/Anki-2.1.55%2B-blue)
![License](https://img.shields.io/github/license/kevincar/A2UWID)
![Platform](https://img.shields.io/badge/Platform-Anki%20Desktop-orange)

This Anki add-on extracts **UWorld question IDs** from tags on **selected
cards in the Browser** and copies them as a **comma-separated list** to your
clipboard. It is especially useful for students studying for **USMLE Step 1 or
Step 2** who tag their Anki notes with UWorld question references.

## ✨ Features

- Extracts UWorld question IDs from selected cards.
- Assumes tags of the form: `UWorld**Step**15861` (customizable via regex).
- Skips untagged or unrelated notes.
- Copies result directly to your system clipboard.
- Feedback via Anki’s tooltip system.

## 📸 Example

Suppose you have tags like:

```

UWorld::Step2::15861
UWorld::Step1::10345
UWorld::Step2::15862

```

Selecting these cards and running the add-on will copy this string to your
clipboard:

```

10345, 15861, 15862

```

## 🚀 Installation

### Option 1: From GitHub (Manual)

1. Download this repository as a ZIP.
2. Extract it into your Anki `addons21/` directory.
   - On most systems, this is located at:
     - **Windows:** `C:\\Users\\<you>\\AppData\\Roaming\\Anki2\\addons21`
     - **macOS:** `~/Library/Application Support/Anki2/addons21/`
     - **Linux:** `~/.local/share/Anki2/addons21/`
3. Restart Anki.

### Option 2: From AnkiWeb (when published)

1. Open Anki.
2. Go to `Tools > Add-ons > Get Add-ons...`
3. Enter the AnkiWeb Add-on code: `XXXXXXX` (replace when available)
4. Restart Anki.

---

## 🧠 Usage

1. Open the Anki **Browser**.
2. Select one or more cards with UWorld-style tags.
3. Go to the menu: `Edit > Get UWorld IDs from Cards`.
4. A tooltip will confirm the result was copied to your clipboard.

---

## 🛠️ Customization

The add-on uses a regular expression to extract IDs from tags. By default, it matches tags of the form:

```

UWorld**Step**12345

````

If your tags follow a different format, you can modify the pattern in the code:

```python
pattern = re.compile(r"UWorld::Step\d+::(\d+)$")
````

## 📦 Development

To install from source:

```bash
git clone https://github.com/kevincar/a2uwid-uworld-id-extractor.git
cd anki-uworld-id-extractor
cp -r . ~/.local/share/Anki2/addons21/a2uwid/
```

## 📝 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

## 💡 Contributing

Pull requests, suggestions, and bug reports are welcome. Please open an issue
if you have ideas for improvement or run into a problem!

## 🙌 Acknowledgments

Inspired by the needs of students who blend UWorld and Anki in their board
prep. Thanks to the Anki community and [@dae](https://github.com/dae) for
maintaining the platform.
