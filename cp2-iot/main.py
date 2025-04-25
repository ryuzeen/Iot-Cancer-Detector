import cv2

# Função para detectar características na imagem (exemplo: manchas suspeitas)
def detectar_manchas(imagem):
    # Convertendo a imagem para escala de cinza
    cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    # Aplicando um filtro de suavização
    blur = cv2.GaussianBlur(cinza, (5, 5), 0)
    # Detecção de bordas com Canny
    bordas = cv2.Canny(blur, 100, 200)
    return bordas

# Captura de imagem de uma câmera IoT (substitua com sua câmera real)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Processamento da imagem
    bordas = detectar_manchas(frame)
    
    # Exibindo a imagem com as bordas detectadas
    cv2.imshow("Bordas Detectadas", bordas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
