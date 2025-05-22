# Gerador de Anúncios com Watermark

Este script automatiza a geração de conjuntos de imagens para anúncios, utilizando imagens temáticas organizadas em pastas. Cada anúncio gerado é composto por 10 imagens:

1. Imagem inicial da pasta `capa`
2. Uma imagem aleatória de cada uma das demais pastas intermediárias, embaralhadas
3. Uma imagem final da pasta `fim`

Todas as imagens recebem uma marca d'água (watermark) padronizada.

---

## Estrutura de Pastas Esperada

```
.
├── imagens_anuncios/
│   ├── capa/
│   ├── mosaico/
│   ├── tijolinho/
│   ├── dunas/
│   ├── ripado/
│   ├── cullinans/
│   ├── piazza/
│   ├── floral/
│   ├── almofadinha/
│   └── fim/
├── watermark.png
├── gerar_anuncios.py
```

---

## Como Usar

1. Adicione suas imagens nas respectivas subpastas dentro de `imagens_anuncios/`.
2. Adicione sua imagem de marca d'água como `watermark.png` na raiz do projeto.
3. Execute o script:

```bash
python gerar_anuncios.py
```

4. Digite a quantidade de anúncios que deseja gerar.
5. Será criada uma pasta para cada anúncio, contendo 10 imagens nomeadas sequencialmente com a marca d'água aplicada.

---

## Requisitos

* Python 3.7+
* Pillow (`pip install pillow`)

---

## Características

* Garante que nenhuma imagem se repita entre os anúncios gerados
* Ordena as imagens de forma padronizada (capa -> aleatórias -> fim)
* Aplica automaticamente a marca d'água
* Corrige orientação da imagem usando metadados EXIF

---

## Exemplo de Saída

```
anuncio_1/
├── imagem_1.png  (capa)
├── imagem_2.png  (intermediária 1)
...
├── imagem_10.png (fim)

anuncio_2/
...
```

---

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests com melhorias.
