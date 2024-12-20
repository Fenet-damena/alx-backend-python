from typing import List, Set, Dict, Tuple

# Variables
age : int = 25


x: List[int] = [1]
x: Set[int] = {6, 7}
x: Dict[str, float] = {"field": 2.0}
x: Tuple[int, str, float] = (3, "yes", 7.5)
x: Tuple[int, ...] = (1, 2, 3)

def isChild(age: int) -> bool:
    child : bool
    if age < 18:
        child = True
    else:
        child = False
    return child
        



if __name__ == '__main__':
    print(isChild(age))
    
    from typing import Union, Optional
    x: List[int | str] = [1, "bye"]
    print(x)
    
    x: List[Union[int, str]] = [1, "bye"]
    print(x)
    
    
    x: Optional[str] = "Something"
    
    if x is not None:
        print(x.upper())
    else:
        print(None)
        
    assert x is not None
    print(x.upper())
    
    from typing import Mapping, MutableMapping, Sequence, Iterable
    def f(ints: Iterable[int]) -> list[int]:
        return [str(x) for x in ints]
        
    print(f(range(1, 3)))
    
    def f(my_mapping: Mapping[int, str]) -> list[int]:
        my_mapping[5] = "maybe"
        return list(my_mapping.keys())
        
    print(f({3:'abc', 4:'dfg'}))