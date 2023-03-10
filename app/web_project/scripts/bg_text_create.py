from PIL import Image, ImageDraw, ImageFont


def create_text(text, file_back, file_save_to, font_file):
    BACKGROUND_IMAGE_FILENAME = file_back
    RESULT_IMAGE_FILENAME = file_save_to # отдать
    THE_TEXT = text # Получать с сайта
    FONT_NAME = font_file  # Arial Bold
    
    # Read the background image and convert to an RGB image with Alpha.
    with open(BACKGROUND_IMAGE_FILENAME, 'rb') as file:
        bgr_img = Image.open(file)
        bgr_img = bgr_img.convert('RGBA')  # Give iamge an alpha channel.
        bgr_img_width, bgr_img_height = bgr_img.size
        cx, cy = bgr_img_width//2, bgr_img_height//2  # Center of image.
    
    # Create a transparent foreground to be result of non-text areas.
    fgr_img = Image.new('RGBA', bgr_img.size, color=(32, 43, 56)) # Git balck: (13, 17, 23) Zero: (0, 0, 0, 0) Google doc black: (27, 27, 27) Google white: (255, 255, 255) css (32, 43, 56)
    
    font_size = bgr_img_width//len(THE_TEXT)
    # print(font_size)
    
    font = ImageFont.truetype(FONT_NAME, font_size+128) # Размер шрифта; +128 Для обложки VK.
    
    txt_width, txt_height = font.getsize(THE_TEXT)  # Size of text w/font if rendered.
    tx, ty = cx - txt_width//2, cy - txt_height//2  # Center of text.
    
    mask_img = Image.new('L', bgr_img.size, color=255)
    mask_img_draw = ImageDraw.Draw(mask_img)
    mask_img_draw.text((tx, ty), THE_TEXT, fill=0, font=font, align='center')
    
    res_img = Image.composite(fgr_img, bgr_img, mask_img)
    res_img.save(RESULT_IMAGE_FILENAME)
    #res_img.show()
    return(RESULT_IMAGE_FILENAME)
