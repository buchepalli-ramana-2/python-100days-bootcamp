# Formating name as Title. 
# Create function which takes two inputs as f_name and l_name

def format_name(f_name,l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"
    # name = f_name +" "+l_name
    # return name.title()

formatted_name = format_name("rAmANA","prasANNA")

print(f"Formatted name: {formatted_name}")
