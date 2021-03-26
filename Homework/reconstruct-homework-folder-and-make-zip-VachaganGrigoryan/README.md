# file-operations

I consider you have homework folder with all repository folders which structure looks nearly as follows:

```
--Homework-
     |____homework_1_name-githubUsername
              |____file_1.py
              |____file_2.py
              |____.git
              |____folder_1
                    |____file_1.py
                    |____text_file.txt
                    ...
              |____folder_2
              ...
     |____homework_2_name-githubUsername
     ...
     |____homework_6_name-githubUsername
     ...
```

Write script that create new homework folder zip where file/follder structure are following
```
homework.zip
    |____homework_1_name
              |____file_1.py
              |____file_2.py
              |____folder_1
                    |____file_1.py
                    ...
              |____folder_2
              ...
     |____homework_2_name
     ...
     |____homework_6_name
     ...
```

This means you should keep only homework name, .py files with it's folders and make zip of that folder(do not save new homework folder, use Tempdirectory)
