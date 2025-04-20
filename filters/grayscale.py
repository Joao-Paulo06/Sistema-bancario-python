from PIL import Image

def to_grayscale(image_path, output_path=None):
   
    try:
        img = Image.open(image_path).convert('L')
        if output_path:
            img.save(output_path)
            print(f"Imagem em tons de cinza salva em: {output_path}")
        else:
            img.show()
        return img
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {image_path}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    to_grayscale("input.jpg", "grayscale_output.jpg")