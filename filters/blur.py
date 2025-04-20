from PIL import Image, ImageFilter

def apply_blur(image_path, radius=2, output_path=None):
   
    try:
        img = Image.open(image_path)
        blurred_img = img.filter(ImageFilter.GaussianBlur(radius=radius))
        if output_path:
            blurred_img.save(output_path)
            print(f"Imagem borrada salva em: {output_path}")
        else:
            blurred_img.show()
        return blurred_img
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {image_path}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    apply_blur("input.jpg", 5, "blur_output.jpg")