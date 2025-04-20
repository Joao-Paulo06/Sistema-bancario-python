from PIL import Image

def resize_image(image_path, new_width, new_height, output_path=None):
    
    try:
        img = Image.open(image_path)
        resized_img = img.resize((new_width, new_height))
        if output_path:
            resized_img.save(output_path)
            print(f"Imagem redimensionada salva em: {output_path}")
        else:
            resized_img.show()
        return resized_img
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {image_path}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    resize_image("input.jpg", 300, 200, "resized_output.jpg")