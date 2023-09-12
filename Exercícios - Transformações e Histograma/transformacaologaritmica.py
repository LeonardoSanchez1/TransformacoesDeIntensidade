import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('fractured_spine.tif', 0)  # 0 para carregar a imagem em escala de cinza

# Aplicar a transformação logarítmica com diferentes valores de c
valores_c = [10, 50, 100]  # Você pode ajustar esses valores conforme necessário

for c in valores_c:
    imagem_transformada = c * np.log1p(imagem)  # Aplicando a transformação logarítmica
    imagem_transformada = np.uint8(imagem_transformada)  # Converter de volta para uint8

    # Exibir a imagem transformada
    cv2.imshow(f'Transformacao Logaritmica (c={c})', imagem_transformada)
    cv2.waitKey(0)

# Fechar janelas
cv2.destroyAllWindows()
