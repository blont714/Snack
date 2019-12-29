from PIL import Image
import glob
import os

def resize_img(im_list):
    for im in im_list:
        img = Image.open(im)
        img_resize = img.resize((140, 840))
        img_resize.save(im)


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def get_concat_h_multi(tmp_list):
    _im = Image.open(tmp_list.pop(0))
    for im in tmp_list:
        im = Image.open(im)
        _im = get_concat_h(_im, im)
    return _im

def make_img(im_list):
    for im in im_list:
        name = im[6:]
        im = Image.open(im)
        for i in range(6):
            im_crop = im.crop((0, 140*i, 140, 140*(i+1)))
            im_crop.save('tmp'+str(i)+'.png')
        tmp_list = ['tmp0.png','tmp1.png','tmp2.png','tmp3.png','tmp4.png','tmp5.png']
        get_concat_h_multi(tmp_list).save('output/' + name)

    for i in range(6):
        os.remove('tmp'+str(i)+'.png')



if __name__ == '__main__':
    im_list = glob.glob('input/*')
    print(im_list)
    resize_img(im_list)
    make_img(im_list)
