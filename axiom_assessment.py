import pandas as pd
import sqlite3

data = pd.read_csv("AxioGlobe_Fictional_Product_Data.csv")
#missing product id

missing_product_id = data[data["product_id"].isna()]
data = data.drop(missing_product_id.index)


#missing product names 
missing_products = data[data["product_name"].isna()]
data = data.drop(missing_products.index)

#duplicate ids
duplicate_id = data[data["product_id"].duplicated(keep = False)]
data = data.drop_duplicates(subset= ["product_id"], keep = "first")


#duplicated products
duplicate_product = data[data["product_name"].duplicated(keep = False)]


#invalid category naming
data["category"] = data["category"].str.upper()


#invalid category naming
data["product_name"] = data["product_name"].str.upper()


#inconsistent dimensions

data["width_mm"] = pd.to_numeric(data["width_mm"], errors = "coerce")
data["height_mm"] = pd.to_numeric(data["height_mm"], errors = "coerce")
data["depth_mm"] = pd.to_numeric(data["depth_mm"], errors = "coerce")
data["depth_mm"] = pd.to_numeric(data["depth_mm"], errors = "coerce")
data["weight_kg"] = pd.to_numeric(data["weight_kg"], errors = "coerce")

invalid_dimensions = data[
    (data[["width_mm", "height_mm", "depth_mm", "weight_kg"]].isna().any(axis=1)) |
    (data["width_mm"] <= 0) |
    (data["height_mm"] <= 0) |
    (data["depth_mm"] <= 0) |
    (data["weight_kg"] <= 0)
]

data = data.drop(invalid_dimensions.index)


#missing price
data["unit_price_gbp"] = pd.to_numeric(data["unit_price_gbp"], errors = "coerce")

invalid_prices = data[(data["unit_price_gbp"].isna()) | (data["unit_price_gbp"] < 0)]
data = data.drop(invalid_prices.index)


#inconsistent lead times

inconsistent_days = data[data["lead_time_days"].isna() | (data["lead_time_days"] <= 0) | (data["lead_time_days"] > 365)]
data = data.drop(inconsistent_days.index)

data["currency"] = data["currency"].str.upper()
data.loc[data["currency"] != "GBP", "currency"] = "GBP"

print(data)

data.to_csv("cleaned_products.csv", index = "False")




data = pd.read_csv("cleaned_products.csv")

connection = sqlite3.connect("products.db")

data.to_sql("products", connection, if_exists="replace", index=False)

connection.close()





