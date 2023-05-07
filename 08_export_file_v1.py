import pandas

# Frames and content for export

variable_heading = "\n{-=-=- Variable Costs -=-=-=-}"

variable_dict = {
    "Item": ["Mugs", "Printing", "Packaging"],
    "Quantity": [300, 300, 50],
    "Price": [1, .5, .75]
}

fixed_dict = {
    "Item": ["Rent", "Artwork", "Advertising"],
    "Price": [25, 35, 10]
}

variable_cost = "\n[Variable Costs Sub Total: $2.25]"

variable_frame = pandas.DataFrame(variable_dict)
fixed_frame = pandas.DataFrame(fixed_dict)

# Change dataframe to string (so it can be written to a txt file)
variable_txt = pandas.DataFrame.to_string(variable_frame)
fixed_txt = pandas.DataFrame.to_string(fixed_frame)

fixed_heading = "\n{-=- Fixed Costs -=-}"

product_name = "Custom Mugs"
product_heading = f"+*+*+ {product_name} +*+*+"
product_selling = "\n{=- Selling Information -=}"
profit_target = "Profit Target: $100.00"
required_sales = "Required Sales: $200.00"
recommended_price = "\nRecommended Price is $5.00]"

Fixed_cost = "\n[Fixed Costs Sub Total: $70.00]"

to_write = [product_heading, variable_heading, variable_txt, variable_cost,
            fixed_heading, fixed_txt, Fixed_cost, product_selling,
            profit_target, required_sales, recommended_price]

# Write to file
# create file to hold data (add .txt extension
file_name = "{}.txt".format(product_name)
text_file = open(file_name, "w+")

# heading
for item in to_write:
    text_file.write(item)
    text_file.write("\n\n")

# close file
text_file.close()


print(string_heading)

# Print Stuff
for item in to_write:
    print(item)
