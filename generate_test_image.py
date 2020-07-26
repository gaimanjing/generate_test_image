

# https://www.liaoxuefeng.com/wiki/1016959663602400/1017785454949568

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def generateSourceImage(sourceImageFileName):
    # # 1242 x 2688, iPhone Xs Max
    width = 1242
    height = 2688
    image = Image.new('RGB', (width, height), (255, 255, 255))


    # 创建Draw对象:
    draw = ImageDraw.Draw(image)

    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())

    # # 模糊:
    # image = image.filter(ImageFilter.BLUR)
    image.save(sourceImageFileName, 'jpeg')


def generateImage(sourceImageFileName, fileName, text, font):
    # # 1242 x 2688, iPhone Xs Max
    # width = 1242
    # height = 2688
    # image = Image.new('RGB', (width, height), (255, 255, 255))
    image = Image.open(sourceImageFileName)


    # 创建Draw对象:
    draw = ImageDraw.Draw(image)

    # # 填充每个像素:
    # for x in range(width):
    #     for y in range(height):
    #         draw.point((x, y), fill=rndColor())

    # 输出文字:
    # draw.text((60, 100), text, font=font, fill=rndColor2())
    draw.text((60, 1000), text, font=font, fill=(0, 0, 0))

    # # 模糊:
    # image = image.filter(ImageFilter.BLUR)
    image.save(fileName, 'jpeg')



def batchGenerateImage(sourceImageFileName, count):
    font = ImageFont.truetype('Arial.ttf', 400)
    prefix = random.randint(0, 1000)
    dirname = 'output/'
    char = rndChar() + rndChar()
    for i in range(count):
        fileName = dirname + str(prefix) + 'image' + str(i) + '.jpg'
        text = char + str(i)
        generateImage(sourceImageFileName, fileName, text, font)



sourceImageFileName = (rndChar() + rndChar() + '_soureImage.jpg')
generateSourceImage(sourceImageFileName)
batchGenerateImage(sourceImageFileName, 20)