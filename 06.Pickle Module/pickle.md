**What is pickle module?**  
It is used to convert python objects into a byte stream and store them in a file, and later restore them back to Python objects.  
This process is called:
    Pickling --> Python object -> bytes
    Unpickling --> Bytes -> Python objects

**What objects can be pickled?**  
int, float, str, list, tuple, dict, set, custom classes and objects, nested objects  

**What objects cannot be pickled?**  
open file objects, database connections, sockets, lambda functions

**Basic Pickle functions**  
| Function         | Purpose               |  
| ---------------- | --------------------- |  
| `pickle.dump()`  | Write object to file  |  
| `pickle.load()`  | Read object from file |  
| `pickle.dumps()` | Object ➜ bytes        |  
| `pickle.loads()` | Bytes ➜ object        |  


