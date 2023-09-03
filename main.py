from rembg import remove
from PIL import Image
from pyfiglet import Figlet

figlet = Figlet(font="slant")
print(figlet.renderText("Photoshop"))

input_a = input("Ведите путь до до фотографий : ")
input_b = input("Ведите имя конечного файла : ")
input_v = f"{input_b}.png"

intu = Image.open(str(input_a))
output = remove(intu)
output.save(input_v)

print(input_v)
