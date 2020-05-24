import youtube_dl 
banner = '''
  __  __                _      _______      _            ___  
 |  \/  |              | |    |__   __|    | |          |__ \ 
 | \  / |  ___   _ __  | |_  ___ | | _   _ | |__    ___    ) |
 | |\/| | / _ \ | '_ \ | __|/ _ \| || | | || '_ \  / _ \  / / 
 | |  | || (_) || | | || |_|  __/| || |_| || |_) ||  __/ / /_ 
 |_|  |_| \___/ |_| |_| \__|\___||_| \__,_||_.__/  \___||____|
                                              coded by: @foxeditor
                                              channel: @montelisa
'''
print(banner)
  
ydl_opts = {} 
  
def dwl_vid(): 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
        ydl.download([zxt]) 
  
channel = 1
while (channel == int(1)): 
    link_of_the_video = input("Вставьте ссылку на видео из YouTube:") 
    zxt = link_of_the_video.strip() 
  
    dwl_vid() 
    channel = int(input("Введите 1 если хотите скачать что-то еще, введите 2 для выхода: ")) 
