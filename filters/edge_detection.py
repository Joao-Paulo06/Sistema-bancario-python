from PIL import Image, ImageFilter

def detect_edges(image_path, output_path=None):
   
    try:
        img = Image.open(image_path).convert('L')  # Converter para tons de cinza para melhor detecção
        edges_img = img.filter(ImageFilter.FIND_EDGES)
        if output_path:
            edges_img.save(output_path)
            print(f"Bordas detectadas e salvas em: {output_path}")
        else:
            edges_img.show()
        return edges_img
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em {image_path}")
        return None

if __name__ == "__main__":
    # Exemplo de uso
    detect_edges("input.jpg", "edges_output.jpg")