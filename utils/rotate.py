from PIL import Image

def rotate_image(image_path, degrees, output_path=None):
   
    try:
        img = Image.open(image_path)
        rotated_img = img.rotate(degrees)
        if output_path:
            rotated_img.save(output_path)
            print(f"Imagem rotacionada salva em: {output_path}")
        else:
            rotated_img.show()
        return rotated_img
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {image_path}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    rotate_image("input.jpg", 90, "rotated_output.jpg")