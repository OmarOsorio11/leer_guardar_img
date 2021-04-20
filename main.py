import cv2


# read img
def read_img(url):
    img = cv2.imread(url, 0)
    return img


# show imagen
def show_img(img):
    cv2.imshow('Imagen', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Write a img
def write_img(img):
    cv2.imwrite('grises.jpg', img)


# main
def main():
    img = read_img('imagen.jpg')
    show_img(img)
    write_img(img)


if __name__ == '__main__':
    main()
