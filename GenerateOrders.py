import pandas as pd
import string
import random as rndm

# List of products
products_list = [
    "KIT-RL-ROLLSGF", "PSH-RL-ROLLSINBAGGF", "PSH-RL-ROLLSINBAGGF", 
    "PKG-CO-CKDONATE", "PSH-EX-OATS", "PKG-TI-ICTWIST", "KIT-SP-CHILI", 
    "ACC-AT-BDAYCONF", "PKG-IN-FLXBLNK", "PSH-SP-LOBSTER", "PSH-SP-BROCCH", 
    "PKG-LN-ZIPSP", "DEMO-PKG-CA-ULTBDAY", "DEMO-ACC-TW-FALLLEAVES", 
    "DEMO-ACC-TW-FALLLEAVES", "DEMO-PKG-ST-BCN"
]

# Generate random external order id 
def generateExternalOrderId():
    return ''.join(rndm.choices(string.ascii_uppercase + string.digits, k=8))

def generateOrders(template_orders_csv, num_orders, output_file="GeneratedOrders.csv"):
    # Read template CSV (take the first row as the "base order")
    template_df = pd.read_csv(template_orders_csv)
    
    # Get sample data from the first row
    base_row = template_df.iloc[0].to_dict()
    
    generated_rows = []

    for i in range(1, num_orders + 1):
        num_items = rndm.randint(2, 5) # Random number of items for an order
        
        external_id = generateExternalOrderId()
        order_name =  "ORDER-" + str(i)
        
        for _ in range(num_items):
            row = {"external-id": external_id, "order-name": order_name}
            # Add all the data from the csv except external-id, order-name, product, quantity
            for cols in template_df.columns.tolist():
                if cols == "external-id" or cols == "order-name" or cols == "product-id-value" or cols == "quantity":
                    continue
                row[cols] = base_row[cols]

            # Select a random product and quantity
            products = rndm.choice(products_list)
            row["product-id-value"] = products
            row["quantity"] = rndm.randint(1, 5)
            
            generated_rows.append(row)

    # Save generated orders to CSV
    generated_df = pd.DataFrame(generated_rows, columns=template_df.columns.tolist())
    generated_df.to_csv(output_file, index=False)
    print(f"✅ Generated {num_orders} orders with multiple products in {output_file}")

if __name__ == "__main__":
    file = input("Enter a csv file with it's path: ")
    orders = int(input("Enter the number of orders you want to generate: "))
    generateOrders(file, orders)
