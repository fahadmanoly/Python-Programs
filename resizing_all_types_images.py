from PIL import Image, UnidentifiedImageError
import os
import svgpathtools
import re

valid_extensions = ('.bmp', '.jpg', '.jpeg', '.png', '.webp', '.svg') 

def resize_image(input_path, output_path, width, height):
    try:
        # Validate the file format
        input_dir, file_name = os.path.split(input_path)
        file_name, file_extension = os.path.splitext(file_name)
        file_extension = file_extension.lower()
        
        if file_extension not in valid_extensions:
            raise ValueError(f"Invalid file extension '{file_extension}'. The valid extensions are {tuple(valid_extensions)}")
        
        # Open and resize the image, using bilinear interpolation
        if file_extension == '.svg':
            # For SVG files, first get the width and height of the SVG image
            with open(input_path, 'r') as f:
                svg_text = f.read()
            
            # Find width and height attributes in the SVG text
            width_match = re.search('width="([0-9.]+)"', svg_text)
            height_match = re.search('height="([0-9.]+)"', svg_text)
            
            if width_match and height_match:
                svg_width = float(width_match.group(1))
                svg_height = float(height_match.group(1))
            else:
                raise ValueError("Width and height attributes not found in SVG file.")
            
            # Scale the SVG path
            def scale(p, scale_x, scale_y):
                return svgpathtools.Path(p.commands, scale_x*p.vertices[0], scale_y*p.vertices[1], scale_x*p.vertices[2], scale_y*p.vertices[3], scale_x*p.vertices[4], scale_y*p.vertices[5])
            
            path_list = list(svgpathtools.Path(svg_text).iter_segments())
            scaled_path_list = [scale(p, width/svg_width, height/svg_height) for p in path_list]
            
            # Create a new SVG file with the resized path
            with open(output_path, 'w') as f:
                f.write('<svg width="' + str(width) + '" height="' + str(height) + '">\n')
                for p in scaled_path_list:
                    f.write(str(p) + '\n')
                f.write('</svg>')
            print(f"The SVG image at {input_path} has been resized and saved at {output_path}.")
        else:
            img = Image.open(input_path)
            img = img.resize((width, height), Image.BILINEAR)
            img.save(output_path)
            print(f"The image at {input_path} has been resized and saved at {output_path}.")

    except UnidentifiedImageError as e:
        print(f"Error: {e}. The file is not a valid image.")

    except ValueError as e:
        print(f"Error: {e}. Please provide a valid image with an extension of {valid_extensions}.")

    except Exception as e:
        print(f"Error: {e}. An unexpected error occurred.")

# To use this function, call it with an input path and an output path
resize_image('your_input_path', 'your_output_path', 1000, 1000)