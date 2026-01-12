**What is Regular Expression?**  
Regex is a pattern used to :
* search text
* match text
* validate text
* extract parts of text
* replace text  
In simple words its is an advanced string search.  

Python regex lives in the re module

**Row Strings(r"")**  
Python uses spacial characters like :
\n \t \d \w  

also python uses \ for escape sequence  

\d -> python thinks escape sequence, to fix use : r"/d"  


**Regex functions**  
1. re.search()  
   * finds first match only  
   * returns a match object if found or None
2. re.match()  
    * matches only at the beginning  
   

    Use search() most of the time      
    Use match() only when position matters
3. re.findall()  
   * returns list of matches
   * no match object -> just strings
4. re.finditer()  
   * returns iterator of match objects
   * best when you need positions


**Meta Characters**  
1.      .  -> Any characters
2.      ^  -> Start of string
3.      $  -> End of string
4.      *  -> 0 or more
5.      +  -> 1 or more
6.      ?  -> 0 or 1
7.     {} -> Exact count
8.     [] -> Character set
9.     () -> group
10.    `  -> `
11.     \ -> Escape

**Character Classes**  
* \d → Digit (0-9)
* \w → Word character (A-Z a-z 0-9 _)
* \s → Whitespace (Tab, space, newline)
* \D  → not digit
* \W  → not word
* \S  → not space


