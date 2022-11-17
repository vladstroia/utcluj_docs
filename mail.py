import yagmail
yag = yagmail.SMTP('fisadisciplinei', 'parola12345678')
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('vlad.stroia@prelucram.ro', f'salut {"vlad"}', contents)
