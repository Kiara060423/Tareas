import cv2


# Cargar la imagen real en la escala de grises
img = cv2.imread('cartas.jpg',0)

# Detectar bordes con el algoritmo de Canny
bordeCanny = cv2.Canny(img,100,200)

#mostrar ventanas
cv2.imshow('original',img)
cv2.imshow('canny',bordeCanny)

# Esperar tecla y cerrar
cv2.waitKey(0)
