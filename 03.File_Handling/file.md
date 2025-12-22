**What's file handling?**

It means creating, opening, reading, writing,
updating and deleting files using python.

File are used to:

* Store data permenently
* Read saved data later
* To log information
* To work with csv, json config files

**Types of file**
* Text files -> .txt, .csv, .log, .json
* Binary files -> .jpg, .png, .pdf, exe

**Create Mode ("x")  
It will create a new file, but raise an error if the file already exist, it will allow writing on files, but read and delete aren't allowed.


**Read Mode ("r")**  
This will read the file if file exist, if not it will raise an error.

**Write Mode ("w")**  
This will write into a file, if the file already exist, it deletes the existing data and write the new data.
If not it will create a new file and write the data into it.You can't read the data using "w" mode, it is only for writing

**Append Mode ("a")  
This will add new data at the end of the file without removing the existing data on the file.
If the file exists, it will keep old data  
if the file not exist, it will create a new file and add data on it  
Only for writing, doesn't allow to read


