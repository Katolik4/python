# komendy esptool

    esptool.py --port /dev/ttyUSB0 erase_flash
    esptool.py --port /dev/ttyUSB0 flash_id


# komendy rshell

    sudo rshell --buffer-size=30 --port /dev/ttyUSB0 

# micropython unix
    git clone git@github.com:micropython/micropython-esp32.git
    sudo apt install libffi6 libffi-dev
    cd ports/unix
    sudo make axtls
    sudo make
aby z każdego miejsca w systemie był widziany `micropython`  

    sudo ln -s $(pwd)/micropython /usr/local/bin/micropython

- upip  
instalacja biblioteki - instaluje domyślnie w `$HOME/.micropython/lib/`  
(zobacz: `micropython -m upip`)

      micropython -m upip install micropython-pystone