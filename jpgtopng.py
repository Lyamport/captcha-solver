from PIL import Image

for i in range(1, 1000):
    im = Image.open(f"C:\\Users\VAVAN\Desktop\\telegram\captcha(1)\captchas\c{i}.jpg")
    im.save(f"C:\\Users\VAVAN\PycharmProjects\pythonProject5\Datasets\captcha_images_v2\c{i}.png")