from PIL import Image, ImageDraw, ImageFont
import random

COLORS = [
    {
        "text": "ЗЕЛЁНЫЙ",
        "color": (0, 255, 0, 255)
    },
    {
        "text": "КРАСНЫЙ",
        "color": (255, 0, 0, 255)
    },
    {
        "text": "ЖЁЛТЫЙ",
        "color": (255, 255, 0, 255)
    },
    {
        "text": "СИНИЙ",
        "color": (0, 0, 255, 255)
    },
    {
        "text": "ОРАНЖЕВЫЙ",
        "color": (255, 128, 0, 255)
    },
    {
        "text": "ФИОЛЕТОВЫЙ",
        "color": (127, 0, 255, 255)
    },
    {
        "text": "РОЗОВЫЙ",
        "color": (255, 0, 127, 255)
    }
]

IMAGE_RESOLUTION = (1024, 512)

WORDS_NUM = 40

WORDS_PER_LINE = 5

FONT_SIZE = 24

LINE_INTERVAL = 1

STROKE_WIDTH = 1

WORD_SPACE = 200


img = Image.new('RGBA', IMAGE_RESOLUTION, color=(255, 255, 255, 0))

d = ImageDraw.Draw(img)
unicode_font = ImageFont.truetype("DejaVuSans.ttf", FONT_SIZE)

x, y = 10, 10

answers = []

for i in range(WORDS_NUM):
    word_text = random.randint(0, len(COLORS) - 1)
    word_color = random.randint(0, len(COLORS) - 1)

    while answers and word_color == answers[-1]:
        word_color = random.randint(0, len(COLORS) - 1)

    answers.append(word_color)

    d.text((x, y), COLORS[word_text]["text"], fill=COLORS[word_color]["color"], font=unicode_font, language="ru",
           stroke_width=STROKE_WIDTH)

    x += WORD_SPACE
    if i % WORDS_PER_LINE == WORDS_PER_LINE - 1:
        x, y = 10, y + FONT_SIZE * (1 + LINE_INTERVAL)

img.save('stroop_test.png')

img = Image.new('RGBA', IMAGE_RESOLUTION, color=(255, 255, 255, 255))

d = ImageDraw.Draw(img)

x, y = 10, 10

for i in range(WORDS_NUM):
    d.text((x, y), COLORS[answers[i]]["text"], fill=(0, 0, 0, 255), font=unicode_font, language="ru",
           stroke_width=STROKE_WIDTH)

    x += WORD_SPACE
    if i % WORDS_PER_LINE == WORDS_PER_LINE - 1:
        x, y = 10, y + FONT_SIZE * (1 + LINE_INTERVAL)


img.save('stroop_check.png')