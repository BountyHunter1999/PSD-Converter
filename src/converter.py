from psd_tools import PSDImage


filepath = "data/fahrenheit fridays 7.psd"
filename = filepath.split(".")[0]
psd = PSDImage.open(filepath)
# psd.composite().save(filename.split(".")[0]+".png")

# Access the layers metadata
layers = psd._layers

# Print the layers metadata
# print(layers)

# Iterate through the layers
for layer in layers:
    # Print the layer name and visibility status
    # print(f"Layer Name: {layer.name}, Visible: {layer.visible}")
    
    # Check if the layer has text
    for nested_layer in layer._layers:
        if nested_layer.kind == "type":
            # Extract the text
            text = nested_layer.text
            print(f"Layer Name: {nested_layer.name}, Text: {nested_layer.text}")
    
    print()

# for layer in psd:
#     print(layer)
#     layer_image = layer.composite()
#     layer_image.save("%s/%s.png" % (filename, layer.name))