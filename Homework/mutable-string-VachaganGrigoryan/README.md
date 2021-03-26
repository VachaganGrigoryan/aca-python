# Mutable-String

Create MutableString class that

1. will inherit from MutableSequence from collections.abc

2. will have following methods:
   __ getitem__(self, item),  __ setitem__(self, item, value),  __ str__(self), __ len__(self), __ iter__(self), __ repr__(self), __ add__(self, string),          __ len__(self), __ iter__(self)
   
   title(self), capitalize(self), center(self, width, fill=None),
   
   upper(self), lower(self), startswith(self, string),  endswith(self, string),
   
   find(self, string, start=None, end=None), rfind(self, s, start=None, end=None),
   
   index(self, string, start=None, end=None), rindex(self, string, start=None, end=None), 
   
   split(self, symbol), replace(self, old, new), rreplace(self, old, new), 
   
   isdigit(self), isalpha(self), isalnum(self), islower(self), isupper(self), isspace(self), istitle(self), 
   
   join(self, array), format(self, * args, ** kwargs),
   
   ord(self, c), chr(self, d),
   
   count(self, string, start=None, end=None),

   lstrip(self, c=None), rstrip(self, c=None), strip(self, c=None)
