import os

os.chdir(r'd:/music')

lrc_path = './lrc/'
music_path = './'

music_list = os.listdir(music_path)
lrc_list = os.listdir(lrc_path)

for music_name in music_list:
    if os.path.isfile(music_path + music_name) and music_name.find("-") > 0 and music_name.find("HOYO") < 0:
        # print(music_name)
        author = music_name.split('-')[0]
        # print(author)
        song = music_name.split('-')[1][:-4]
        # print(song)
        for lrc_name in lrc_list:
            # print(lrc_name)
            # print(lrc_name.find(author))
            # print(lrc_name.find(song))
            if lrc_name.find(author) >= 0 and lrc_name.find(song) >= 0:
                
                print(lrc_name)
                print (music_name)

                if music_name[:-3] + 'lrc' in lrc_list:
                    break

                os.chdir(lrc_path)                    
                lrc_list.remove(lrc_name)
                os.rename(lrc_name,music_name[:-3] + 'lrc')
                os.chdir('..')
                break

lrc_list = os.listdir(lrc_path)
for lrc_waste in lrc_list:
    if lrc_waste.split('_')[-1] == 'qm.lrc':
        os.remove(lrc_path + lrc_waste)