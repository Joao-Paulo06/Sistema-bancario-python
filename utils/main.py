from image_processing_package.filters import grayscale, blur, edge_detection
from image_processing_package.utils import resize, rotate

image_file = "input.jpg"

grayscale.to_grayscale(image_file, "output_grayscale.jpg")
blur.apply_blur(image_file, 10, "output_blur.jpg")
edge_detection.detect_edges(image_file, "output_edges.jpg")

resize.resize_image(image_file, 150, 150, "output_resized.jpg")
rotate.rotate_image(image_file, -45, "output_rotated.jpg")