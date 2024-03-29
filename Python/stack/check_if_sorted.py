

# Given a stack, a function is_sorted accepts a stack as a parameter and returns true if said stack is sorted. 
# A stack is considered sorted if it increases from bottom-most element to top-most element. 


def check_if_sorted(stack):
    stg = []
  
    for i in range(len(stack)):
        if len(stack) == 0:
            break
          
        first_val = stack.pop()
        if len(stack) == 0:
            break
          
        second_val = stack.pop()
        if first_val < second_val:
            return False
          
        storage_stack.append(first_val)
        stack.append(second_val)

    # backup stack saved in stg(storage)
    for i in range(len(stg)):
        stack.append(stg.pop())

    return True
