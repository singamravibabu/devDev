# Files

## Two Types of Files:
1. Text Files
    - Contains one or more lines, each line contains characters.
    - In a text file, each line ends with new line (\n) character.
        - On Windows, this is character (\n) is sometimes preceded by a carriage return character (\r).
    - Common types:
        TXT Files
        CSV Files
        JSON Files
        XML Files
        HTML Files
2. Binary Files
    - Any file that isn't a text file.
    - Binary files typically contain sequence of bytes that need to be interpreted as something other than text characters.
    - Common types:
        Compiled program files
        Image files
        Audio files
        Video files
        Database files
        Compressed files

## The sequence of the file operations
1. Open the file.
2. Write data to the file or read data from the file.
3. Close the file.

### 1. Open a file
- When a file opened using open() function, Python creates a file object.
- After a file object is created we can use the methods of the file object to work with the file.
- The built-in function `open()` function:
    open(file, mode)

    - file: file name, sometimes including its path
    - mode: 
        - r (Read):
            -> If the file doesn't exists, this mode causes a file not found error.
        - w (Write):
            -> If the file doesn't exists, this mode creates it.
            -> If the file already exists, this mode erases all existing data from the file.
        - a (Append)
            -> If the file doesn't exits, this mode creates it.
            -> If the file already exists, this mode appends the data to the end of the time.
        - b (Binary)
            -> Use for binary files along with "r" and "w" mode.

> Note: Every file that we open must be closed.

### 2. Closing a file
- Use `close()` method to close an opened file-object.
