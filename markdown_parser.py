import os
import shutil

targets = ['1.md', '2.md', '3.md', '4.md', '5.md', '6.md', '7.md', '8.md']

for target in targets:
    # target_file = "./test.md"
    target_file = './mds/' + target
    index = target.split('.')[0]
    print('####' + target_file + '####')
    f = open(target_file, 'r')

    imgs = []
    check = False
    img_path = ''
    img_description = ''
    for line in f.readlines():
        if check == True:
            img_description = 'pic' + line.split(' ')[1]
            imgs.append((img_path, img_description))
            img_path = ''
            img_description = ''
            check = False
        if line.startswith("!["):
            img_path = line.split("](")[1].split(")")[0]
            check = True

    f.close()

    for img in imgs:
        print(img)
        src = img[0]
        if src.startswith('http'):
            os.system("curl " + src + '> ' + './mds/new_imgs/' + str(index) + '/' + img[1])
            continue
        src = './mds/' + src[2:]
        dst = './mds/new_imgs/' + str(index) + '/' + img[1] + '.png'
        shutil.copyfile(src, dst)
        print(src + ' -> ' + dst)




