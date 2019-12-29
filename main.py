from PIL import Image, ImageFont, ImageDraw
import config
import data

image = Image.open(config.BASE_IMAGE_PATH)
draw = ImageDraw.Draw(image)


def create_image_with_text(primary, secondary=None):
	primary_fontsize = 1
	primary_font = ImageFont.truetype(config.PRIMARY_FONT_PATH, primary_fontsize)
	while primary_font.getsize(primary)[0] < config.IMAGE_FRACTION_ADJUST*image.size[0]:
	    primary_fontsize += 1
	    primary_font = ImageFont.truetype(config.PRIMARY_FONT_PATH, primary_fontsize)


	primary_font = ImageFont.truetype(config.PRIMARY_FONT_PATH, primary_fontsize)

	secondary_fontsize = int(config.PRIMARY_SECONDARY_FONTSIZE_RATIO * primary_fontsize)

	secondary_font = ImageFont.truetype(config.SECONDARY_FONT_PATH, secondary_fontsize)

	print ('Primary Font size',primary_fontsize)
	print("secondary Font Size", secondary_fontsize)

	file_name = "test_image.png" if config.TEST else "generated-images/" + primary + ".png"

	draw.text(config.PRIMARY_TEXT_COORDINATES, primary, font=primary_font)
	if secondary:
		y_coordinate = (image.size[1] - primary_fontsize) * config.ADUST_PRIMARY_SECONDARY_DIS
		draw.text((config.PRIMARY_TEXT_COORDINATES[0], y_coordinate), secondary, font=secondary_font)
	image.save(file_name)
	return




if config.TEST:
	create_image_with_text(primary="Hello World if \n this is cool \n", secondary="Something")
else:
	for data in data.IMAGE_DATA:
		create_image_with_text(primary=data.get("primary"), secondary=data.get("secondary"))



