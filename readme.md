# EasyBackup

I needed a simple backup script that also included rotation of the number of backups, but couldn't find one. Built this, hope somebody can use it too!

## Installation

No installation required. Yes, you need Python 3 but that's about it. Clone the repo and voila, you're set.

```bash
apt install python3
git clone https://github.com/Nexz/easybackup.git
cd easybackup
chmod +x easy-backup.py
```
;-)

## Usage

```
usage: easy-backup.py [-h] [--no-rotation] [--max-backups MAX_BACKUPS]
                      [--prepend PREPEND]
                      source destination

positional arguments:
  source                The directory that contains the files to be backupped
  destination           The destination of the backups. Dated directories will
                        be created in this folder

optional arguments:
  -h, --help            show this help message and exit
  --no-rotation         Turn off backup rotation
  --max-backups MAX_BACKUPS
                        Defines the maximum number of backups to be stored in
                        the destination
  --prepend PREPEND     Defines a different string to prepend to individual
                        backups
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate. Haha just kidding, no tests here.

## License
[MIT](https://choosealicense.com/licenses/mit/)
