import cv2

img = cv2.imread('cartas.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: No se pudo cargar la imagen 'cartas.jpg'")
    print("Asegúrate de que el archivo existe en el directorio actual:", cv2.os.getcwd())
    exit()

borde_canny = cv2.Canny(img, 100, 200)

cv2.imshow('Imagen Original', img)
cv2.imshow('Bordes Canny', borde_canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
