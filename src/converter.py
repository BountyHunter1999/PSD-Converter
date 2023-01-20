from psd_tools import PSDImage

import os
import argparse

# filepath = "data/fahrenheit fridays 7.psd"
filepath = "data/fahrenheit fridays 8.psd"


# Print the layers metadata
# print(layers)



def get_layer_data(layers):
    # Iterate through the layers
    for layer in layers:
        # Print the layer name and visibility status
        # print(f"Layer Name: {layer.name}, Visible: {layer.visible}")
        
        # Check if the layer has text
        # print("Layer Name: ", layer.name)
        if layer.kind == "type":
            # Extract the text
            text = layer.text
            print(f"> Layer Name: {layer.name}, Text: {text}")
        if layer.kind == "group":

            if layers_ := layer._layers:
                get_layer_data(layers_)
                print()
            

# for layer in psd:
#     print(layer)
#     layer_image = layer.composite()
#     layer_image.save("%s/%s.png" % (filename, layer.name))

def get_filepath():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help="The filepath to the file")
    args = parser.parse_args()
    return args.filepath

if __name__ == "__main__":
    # filepath = get_filepath()
    filename = filepath.split(".")[0]
    psd = PSDImage.open(filepath)
    # psd.composite().save(filename.split(".")[0]+".png")

    # Access the layers metadata
    layers = psd._layers
    get_layer_data(layers)
    