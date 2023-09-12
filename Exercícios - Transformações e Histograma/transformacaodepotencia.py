import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('fractured_spine.tif', 0)  # 0 para carregar a imagem em escala de cinza

# Aplicar a transformação de potência com diferentes valores de y
valores_y = [0.5, 1.0, 1.5]  # Você pode ajustar esses valores conforme necessário
c = 1

for y in valores_y:
    imagem_transformada = c * np.power(imagem, y)  # Aplicando a transformação de potência
    imagem_transformada = np.uint8(imagem_transformada)  # Converter de volta para uint8

    # Exibir a imagem transformada
    cv2.imshow(f'Transformacao de Potencia (y={y}, c={c})', imagem_transformada)
    cv2.waitKey(0)

# Fechar janelas
cv2.destroyAllWindows()
