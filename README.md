# Demo-Order-Generator

A Python utility to generate synthetic order data by replicating the structure of an existing template CSV—ideal for testing, demos, or data pipelines.

---

## 🚀 Features
- Reads a template order CSV and preserves all columns and order-level fields.
- Assigns a **random external ID** for each order and ensures each order has **multiple items**.
- Each item appears as a row with its own `external-id`, `order-name`, `product-id-value`, and `quantity`.
- Retains all other template fields unchanged (e.g., customer info, pricing, address, etc.).
- Outputs a new CSV with the same format as the input template for drop-in usage.

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/VireshShah17/Demo-Order-Generator.git
cd Demo-Order-Generator

Create a virtual env
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies
```bash
pip install -r requirements.txt

Run the generator
python3 GenerateOrders.py 
