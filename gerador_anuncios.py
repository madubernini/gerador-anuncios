import os
import random
from PIL import Image, ImageOps

# Caminhos
PASTA_BASE = "imagens_anuncios"
PASTAS_TEMATICAS = [
    "capa", "mosaico", "tijolinho", "dunas", "ripado",
    "cullinans", "piazza", "floral", "almofadinha", "fim"
]
PASTA_WATERMARK = "watermark.png"

# Parâmetros
qtd_anuncios = int(input("Quantos anúncios deseja gerar? "))

# Carregar watermark
watermark = Image.open(PASTA_WATERMARK).convert("RGBA")
tamanho_alvo = watermark.size

# Registrar imagens já usadas para evitar repetição
imagens_usadas = set()


def aplicar_watermark(imagem_path):
    imagem = Image.open(imagem_path).convert("RGBA")
    imagem = ImageOps.exif_transpose(imagem)
    
    if imagem.size != tamanho_alvo:
        imagem = imagem.resize(tamanho_alvo, Image.Resampling.LANCZOS)
    
    return Image.alpha_composite(imagem, watermark)




def escolher_imagem_unica(pasta):
    caminho_pasta = os.path.join(PASTA_BASE, pasta)
    imagens = [f for f in os.listdir(caminho_pasta) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    random.shuffle(imagens)
    for imagem in imagens:
        caminho = os.path.join(pasta, imagem)
        if caminho not in imagens_usadas:
            imagens_usadas.add(caminho)
            return os.path.join(caminho_pasta, imagem)
    raise Exception(f"Imagens insuficientes na pasta '{pasta}' para evitar repetições.")

# Gerar os anúncios
for i in range(1, qtd_anuncios + 1):
    pasta_anuncio = f"anuncio_{i}"
    os.makedirs(pasta_anuncio, exist_ok=True)

    imagens_anuncio = []

    # 1. Imagem da capa
    imagens_anuncio.append(("capa", escolher_imagem_unica("capa")))

    # 2-9. Demais pastas (exceto capa e fim), em ordem aleatória
    pastas_intermediarias = PASTAS_TEMATICAS[1:-1]
    random.shuffle(pastas_intermediarias)
    for pasta in pastas_intermediarias:
        imagens_anuncio.append((pasta, escolher_imagem_unica(pasta)))

    # 10. Imagem do fim
    imagens_anuncio.append(("fim", escolher_imagem_unica("fim")))

    # Salvar imagens com watermark
    for idx, (pasta_origem, caminho_img) in enumerate(imagens_anuncio, start=1):
        imagem_final = aplicar_watermark(caminho_img)
        nome_arquivo = f"imagem_{idx}.png"
        caminho_saida = os.path.join(pasta_anuncio, nome_arquivo)
        imagem_final.save(caminho_saida)

print(f"\n✅ {qtd_anuncios} anúncios gerados com sucesso!")
