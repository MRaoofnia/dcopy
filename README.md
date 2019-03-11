# dcopy
Some tools to reduce name length

## how does it start?
Copying files from a `fat` filesystem to an `ext-4` i recieved some erors, because file names were longer than the limitations of `ext-4`. so i made this tool.

## how does it work?
It copys all files in the directory which has specified extension -if specified, and shortens the file name and path.

## how to run?
```
dcopy pathToCopyFrom pathToCopyTo [extensions] [-l charactersLimitation]
```
- empty extensions means copy everything.
- default value for characters limitation is 255.

## examples
```
dcopy /home/user/mycodes /home/codes py,pyc,dat -l 255
dcopy ./ /home
```
